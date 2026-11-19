$ErrorActionPreference='Stop'
$root='\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\deliverables\report_revision_20261028'
$tempRoot=Join-Path $env:LOCALAPPDATA 'Temp\dl_report_revision_20261028'
$sourcePath=Join-Path $tempRoot 'original.docx'
$cleanPath=Join-Path $tempRoot 'Framework_revised_20261028.docx'
$nativePath=Join-Path $tempRoot 'tracked_native.xml'
$word=$null;$original=$null;$revised=$null;$comparison=$null
try {
    $word=New-Object -ComObject Word.Application
    $word.Visible=$false;$word.DisplayAlerts=0
    $original=$word.Documents.Open($sourcePath,$false,$true)
    $sourceText=$original.Content.Text
    if ($original.Comments.Count -gt 0) {$original.DeleteAllComments()}
    $revised=$word.Documents.Open($cleanPath,$false,$true)
    $cleanText=$revised.Content.Text
    Write-Output 'Comparing original and revised reports with native Word.'
    $comparison=$word.CompareDocuments($original,$revised,2,1,$false,$true,$true,$true,$true,$true,$true,$true,$false,$false,'Report revision',$true)
    $count=$comparison.Revisions.Count
    $comparison.TrackRevisions=$true
    $comparison.ShowRevisions=$true
    [System.IO.File]::WriteAllText($nativePath,$comparison.WordOpenXML,[Text.UTF8Encoding]::new($false))
    Copy-Item -LiteralPath $nativePath -Destination "$root\qa\tracked_native.xml" -Force
    # Save the delivery through Word so package metadata and namespaces are native.
    $trackedPath=Join-Path $tempRoot 'comparison_delivery.docx'
    $comparison.SaveAs2($trackedPath,16)
    Copy-Item -LiteralPath $trackedPath -Destination "$root\Framework_revised_20261028_tracked.docx" -Force
    Write-Output "Native comparison captured: $count revisions."
    $comparison.AcceptAllRevisions()
    $comparison.TrackRevisions=$false
    foreach ($toc in $comparison.TablesOfContents) {[void]$toc.Update()}
    foreach ($tof in $comparison.TablesOfFigures) {[void]$tof.Update()}
    $comparison.Repaginate()
    $accepted=$comparison.Content.Text
    [System.IO.File]::WriteAllText("$root\qa\tracked_accepted_text.txt",$accepted,[Text.UTF8Encoding]::new($false))
    [System.IO.File]::WriteAllText("$root\qa\clean_word_text.txt",$cleanText,[Text.UTF8Encoding]::new($false))
    $comparison.Close(0);$comparison=$null
    $comparison=$word.Documents.Open($nativePath,$false,$true)
    $comparison.RejectAllRevisions()
    $rejected=$comparison.Content.Text
    [System.IO.File]::WriteAllText("$root\qa\tracked_rejected_text.txt",$rejected,[Text.UTF8Encoding]::new($false))
    [System.IO.File]::WriteAllText("$root\qa\original_word_text.txt",$sourceText,[Text.UTF8Encoding]::new($false))
    $acceptedExact=($accepted -ceq $cleanText);$rejectedExact=($rejected -ceq $sourceText)
    [PSCustomObject]@{WordRevisionCount=$count;AcceptedTextExact=$acceptedExact;RejectedTextExact=$rejectedExact;NativeFormat='Microsoft Word DOCX via SaveAs2'} | ConvertTo-Json | Set-Content -LiteralPath "$root\qa\comparison_verification.json" -Encoding UTF8
    Write-Output "Accept exact=$acceptedExact; reject exact=$rejectedExact"
}
finally {
    if ($null -ne $comparison) {$comparison.Close(0)}
    if ($null -ne $revised) {$revised.Close(0)}
    if ($null -ne $original) {$original.Close(0)}
    if ($null -ne $word) {$word.Quit()}
}
