$ErrorActionPreference='Stop'
$root='\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\deliverables\results_slides_20261029'
$tempRoot=Join-Path $env:LOCALAPPDATA 'Temp\dl_results_slides_20261029'
New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null
$local=Join-Path $tempRoot 'Updated_results_20261029.pptx'
$pdf=Join-Path $tempRoot 'Updated_results_20261029.pdf'
$preview=Join-Path $tempRoot 'slides'
New-Item -ItemType Directory -Path $preview -Force | Out-Null
Copy-Item -LiteralPath "$root\Updated_results_20261029.pptx" -Destination $local -Force
$app=$null; $deck=$null; $existing=0
try {
    $app=New-Object -ComObject PowerPoint.Application
    $existing=$app.Presentations.Count
    $deck=$app.Presentations.Open($local,-1,0,0)
    $count=$deck.Slides.Count
    if($count -ne 7){throw "Unexpected slide count: $count"}
    $checks=@()
    foreach($slide in $deck.Slides){
        $pictures=0; $overflows=@()
        foreach($shape in $slide.Shapes){
            if($shape.Type -eq 13){$pictures++}
            if($shape.HasTextFrame -eq -1 -and $shape.TextFrame.HasText -eq -1){
                $text=$shape.TextFrame2.TextRange
                if($text.BoundHeight -gt ($shape.Height+2)){$overflows+=$shape.Name}
            }
        }
        if($pictures -ne 1){throw "Slide $($slide.SlideIndex) has $pictures pictures"}
        $checks+=[PSCustomObject]@{Slide=$slide.SlideIndex;Pictures=$pictures;TextOverflowShapes=$overflows}
    }
    Write-Output 'Exporting seven slides with Microsoft PowerPoint.'
    $deck.Export($preview,'PNG',1600,900)
    $deck.SaveAs($pdf,32)
    Copy-Item -LiteralPath $pdf -Destination "$root\Updated_results_20261029.pdf" -Force
    New-Item -ItemType Directory -Path "$root\previews" -Force | Out-Null
    Get-ChildItem -LiteralPath $preview -Filter '*.PNG' | Copy-Item -Destination "$root\previews" -Force
    [PSCustomObject]@{NativePowerPointOpen=$true;Slides=$count;Exporter='Microsoft PowerPoint';SlideChecks=$checks} | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath "$root\qa\powerpoint_verification.json" -Encoding UTF8
    Write-Output "Exported $count slides to PDF and 1600 x 900 previews."
}
finally {
    if($null -ne $deck){$deck.Close()}
    if($null -ne $app -and $existing -eq 0){$app.Quit()}
}
