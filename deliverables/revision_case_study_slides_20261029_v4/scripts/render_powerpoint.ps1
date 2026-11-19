$ErrorActionPreference='Stop'
$root='\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\deliverables\revision_case_study_slides_20261029_v4'
$stem='Updated_case_study_20261029_v4'
$tempRoot=Join-Path $env:LOCALAPPDATA 'Temp\dl_revision_case_study_slides_20261029_v4'
New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null
$local=Join-Path $tempRoot "$stem.pptx"
$pdf=Join-Path $tempRoot "$stem.pdf"
$preview=Join-Path $tempRoot 'slides'
New-Item -ItemType Directory -Path $preview -Force | Out-Null
Copy-Item -LiteralPath "$root\$stem.pptx" -Destination $local -Force
$nativeSlides=@(1,2,6,8,9)
function Get-LeafShapes($items) {
    foreach($shape in $items){
        if($shape.Type -eq 6){Get-LeafShapes $shape.GroupItems}else{$shape}
    }
}
$app=$null; $deck=$null; $existing=0
try {
    $app=New-Object -ComObject PowerPoint.Application
    $existing=$app.Presentations.Count
    $deck=$app.Presentations.Open($local,-1,0,0)
    $count=$deck.Slides.Count
    if($count -ne 9){throw "Unexpected slide count: $count"}
    $checks=@()
    foreach($slide in $deck.Slides){
        $pictures=0; $overflows=@(); $bounds=@(); $connectors=@(); $textShapes=0
        foreach($shape in $slide.Shapes){
            if(($shape.Left -lt -1) -or ($shape.Top -lt -1) -or (($shape.Left+$shape.Width) -gt ($deck.PageSetup.SlideWidth+1)) -or (($shape.Top+$shape.Height) -gt ($deck.PageSetup.SlideHeight+1))){$bounds+=$shape.Name}
        }
        foreach($shape in (Get-LeafShapes $slide.Shapes)){
            if($shape.Type -eq 13){$pictures++}
            if($shape.Connector -eq -1){
                $cf=$shape.ConnectorFormat
                $connectors+=[PSCustomObject]@{Name=$shape.Name;BeginConnected=($cf.BeginConnected -eq -1);EndConnected=($cf.EndConnected -eq -1)}
            }
            if($shape.HasTextFrame -eq -1 -and $shape.TextFrame.HasText -eq -1){
                $textShapes++
                $text=$shape.TextFrame2.TextRange
                if(($text.BoundHeight -gt ($shape.Height+2)) -or ($text.BoundWidth -gt ($shape.Width+2))){$overflows+=$shape.Name}
            }
        }
        $isNative=$nativeSlides -contains $slide.SlideIndex
        $expectedPictures=if($isNative){0}else{1}
        if($pictures -ne $expectedPictures){throw "Slide $($slide.SlideIndex) has $pictures pictures; expected $expectedPictures"}
        $bothConnected=@($connectors | Where-Object {$_.BeginConnected -and $_.EndConnected}).Count
        if($isNative -and $bothConnected -lt 2){throw "Slide $($slide.SlideIndex) does not have enough attached native connectors"}
        $checks+=[PSCustomObject]@{Slide=$slide.SlideIndex;NativeDiagram=$isNative;Pictures=$pictures;TextShapes=$textShapes;Connectors=$connectors;AttachedConnectors=$bothConnected;TextOverflowShapes=$overflows;OutOfBoundsShapes=$bounds}
    }
    Write-Output 'Exporting nine slides with Microsoft PowerPoint.'
    $deck.Export($preview,'PNG',1600,900)
    $deck.SaveAs($pdf,32)
    Copy-Item -LiteralPath $pdf -Destination "$root\$stem.pdf" -Force
    New-Item -ItemType Directory -Path "$root\previews" -Force | Out-Null
    Get-ChildItem -LiteralPath $preview -Filter '*.PNG' | Copy-Item -Destination "$root\previews" -Force
    [PSCustomObject]@{NativePowerPointOpen=$true;Slides=$count;Exporter='Microsoft PowerPoint';SlideChecks=$checks} | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath "$root\qa\powerpoint_verification.json" -Encoding UTF8
    Write-Output "Exported $count slides to PDF and 1600 x 900 previews."
}
finally {
    if($null -ne $deck){$deck.Close()}
    if($null -ne $app -and $existing -eq 0){$app.Quit()}
}
