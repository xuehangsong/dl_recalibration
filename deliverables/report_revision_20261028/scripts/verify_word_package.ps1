$ErrorActionPreference='Stop'
$root='\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\deliverables\report_revision_20261028'
$word=$null; $doc=$null
try {
    $word=New-Object -ComObject Word.Application
    $word.Visible=$false; $word.DisplayAlerts=0
    $doc=$word.Documents.Open("$root\Framework_revised_20261028.docx",$false,$true)
    $cleanRevisions=$doc.Revisions.Count; $cleanComments=$doc.Comments.Count
    if ($cleanRevisions -ne 0 -or $cleanComments -ne 0) {throw 'Clean document contains revisions or comments'}
    $pages=$doc.ComputeStatistics(2); $figures=$doc.InlineShapes.Count
    $text=$doc.Content.Text
    if ($text.Contains('April 2026')) {throw 'Stale title-page date'}
    [System.IO.File]::WriteAllText("$root\qa\clean_word_text.txt",$text,[Text.UTF8Encoding]::new($false))
    $doc.Close(0); $doc=$null
    $doc=$word.Documents.Open("$root\Framework_revised_20261028_tracked.docx",$false,$true)
    $trackedRevisions=$doc.Revisions.Count
    if ($trackedRevisions -eq 0) {throw 'No revisions in tracked document'}
    $doc.RejectAllRevisions()
    $original=[System.IO.File]::ReadAllText("$root\qa\original_word_text.txt")
    if ($doc.Content.Text -cne $original) {throw 'Repackaged reject-all mismatch'}
    $doc.Close(0); $doc=$null
    $doc=$word.Documents.Open("$root\Framework_revised_20261028_tracked.docx",$false,$true)
    $doc.AcceptAllRevisions()
    $doc.TrackRevisions=$false
    $doc.Repaginate()
    foreach ($toc in $doc.TablesOfContents) {[void]$toc.Update()}
    foreach ($tof in $doc.TablesOfFigures) {[void]$tof.Update()}
    [System.IO.File]::WriteAllText("$root\qa\tracked_accepted_text.txt",$doc.Content.Text,[Text.UTF8Encoding]::new($false))
    [PSCustomObject]@{
        CleanPages=$pages; CleanInlineImages=$figures; CleanRevisions=$cleanRevisions; CleanComments=$cleanComments;
        RepackagedTrackedOpens=$true; RepackagedTrackedRevisions=$trackedRevisions; RepackagedRejectRestoresOriginal=$true;
        FieldsUpdated=$true; ContentsUpdated=$true
    } | ConvertTo-Json | Set-Content -LiteralPath "$root\qa\word_verification.json" -Encoding UTF8
    Write-Output "Verified delivered DOCX files: $pages pages, $figures images, $trackedRevisions tracked revisions."
}
finally {if($null -ne $doc){$doc.Close(0)};if($null -ne $word){$word.Quit()}}
