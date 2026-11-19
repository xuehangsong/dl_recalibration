$ErrorActionPreference='Stop'
$root='\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\deliverables\revision_case_study_slides_20261029_v4'
$stem='Yilin_original_figures_20261029'
$tempRoot=Join-Path $env:LOCALAPPDATA 'Temp\dl_yilin_original_figures_20261029_v4'
New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null
$local=Join-Path $tempRoot "$stem.pptx"
$pdf=Join-Path $tempRoot "$stem.pdf"
$preview=Join-Path $tempRoot 'source_previews'
New-Item -ItemType Directory -Path $preview -Force | Out-Null
Copy-Item -LiteralPath "$root\$stem.pptx" -Destination $local -Force
$app=$null; $deck=$null; $existing=0
try {
    $app=New-Object -ComObject PowerPoint.Application
    $existing=$app.Presentations.Count
    $deck=$app.Presentations.Open($local,-1,0,0)
    $count=$deck.Slides.Count
    if($count -ne 5){throw "Unexpected source slide count: $count"}
    $checks=@()
    foreach($slide in $deck.Slides){
        $pictures=0; $overflows=@(); $bounds=@(); $textShapes=0
        foreach($shape in $slide.Shapes){
            if(($shape.Left -lt -1) -or ($shape.Top -lt -1) -or (($shape.Left+$shape.Width) -gt ($deck.PageSetup.SlideWidth+1)) -or (($shape.Top+$shape.Height) -gt ($deck.PageSetup.SlideHeight+1))){$bounds+=$shape.Name}
            if($shape.Type -eq 13){$pictures++}
            if($shape.HasTextFrame -eq -1 -and $shape.TextFrame.HasText -eq -1){
                $textShapes++
                $text=$shape.TextFrame2.TextRange
                if(($text.BoundHeight -gt ($shape.Height+2)) -or ($text.BoundWidth -gt ($shape.Width+2))){$overflows+=$shape.Name}
            }
        }
        if($pictures -ne 1){throw "Source slide $($slide.SlideIndex) has $pictures pictures; expected one"}
        if($bounds.Count -gt 0){throw "Source slide $($slide.SlideIndex) out-of-bounds shapes: $bounds"}
        if($overflows.Count -gt 0){throw "Source slide $($slide.SlideIndex) text overflow: $overflows"}
        $checks+=[PSCustomObject]@{Slide=$slide.SlideIndex;Pictures=$pictures;TextShapes=$textShapes;TextOverflowShapes=$overflows;OutOfBoundsShapes=$bounds}
    }
    $deck.Export($preview,'PNG',1600,900)
    $deck.SaveAs($pdf,32)
    Copy-Item -LiteralPath $pdf -Destination "$root\$stem.pdf" -Force
    New-Item -ItemType Directory -Path "$root\source_previews" -Force | Out-Null
    Get-ChildItem -LiteralPath $preview -Filter '*.PNG' | Copy-Item -Destination "$root\source_previews" -Force
    [PSCustomObject]@{NativePowerPointOpen=$true;Slides=$count;Exporter='Microsoft PowerPoint';ExistingPresentationsPreserved=$existing;SlideChecks=$checks} | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath "$root\qa\source_companion_powerpoint_verification.json" -Encoding UTF8
    Write-Output "Exported $count source slides to PDF and 1600 x 900 previews."
}
finally {
    if($null -ne $deck){$deck.Close()}
    if($null -ne $app -and $existing -eq 0 -and $app.Presentations.Count -eq 0){$app.Quit()}
}
