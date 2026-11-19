param([switch]$SkipComparison)
$ErrorActionPreference = 'Stop'
$root = '\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\deliverables\report_revision_20261028'
$source = '\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\final report\Framework_revision.docx'
$tempRoot = Join-Path $env:LOCALAPPDATA 'Temp\dl_report_revision_20261028'
New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null
$inputPath = Join-Path $tempRoot 'Framework_revised_20261028.docx'
$sourcePath = Join-Path $tempRoot 'original.docx'
$cleanPath = Join-Path $tempRoot 'Framework_revised_20261028.docx'
$pdfPath = Join-Path $tempRoot 'Framework_revised_20261028.pdf'
$trackedPath = Join-Path $tempRoot 'Framework_revised_20261028_tracked.docx'
Copy-Item -LiteralPath "$root\qa\Framework_20261028_before_word.docx" -Destination $inputPath -Force
Copy-Item -LiteralPath $source -Destination $sourcePath -Force
if (Test-Path -LiteralPath "$root\qa\pdf_export_target.pdf") {
    Copy-Item -LiteralPath "$root\qa\pdf_export_target.pdf" -Destination $pdfPath -Force
}
$word=$null; $doc=$null; $original=$null; $comparison=$null
try {
    Write-Output 'Creating isolated Word instance.'
    $word=New-Object -ComObject Word.Application
    $word.Visible=$false
    $word.DisplayAlerts=0
    Write-Output 'Opening assembled document.'
    $doc=$word.Documents.Open($inputPath,$false,$false)
    Write-Output 'Document opened.'
    $doc.TrackRevisions=$false
    Write-Output 'Tracking disabled.'
    $doc.ShowRevisions=$false
    Write-Output 'Revision display disabled.'
    if ($doc.Revisions.Count -gt 0) {throw 'Unexpected revisions in assembled clean document'}
    Write-Output 'Revision count checked.'
    if ($doc.Comments.Count -gt 0) {$doc.DeleteAllComments()}
    Write-Output 'Comments checked; saving clean copy.'
    $doc.Save()
    Write-Output 'Updating fields and contents.'
    [void]$doc.Fields.Update()
    foreach ($toc in $doc.TablesOfContents) {[void]$toc.Update()}
    foreach ($tof in $doc.TablesOfFigures) {[void]$tof.Update()}
    Write-Output 'First pagination.'
    $doc.Repaginate()
    [void]$doc.Fields.Update()
    foreach ($toc in $doc.TablesOfContents) {[void]$toc.Update()}
    foreach ($tof in $doc.TablesOfFigures) {[void]$tof.Update()}
    $doc.Repaginate()
    $doc.Save()
    if ($SkipComparison) {
        $cleanPages=$doc.ComputeStatistics(2)
        $cleanFigures=$doc.InlineShapes.Count
        [System.IO.File]::WriteAllText("$root\qa\clean_word_text.txt",$doc.Content.Text,[Text.UTF8Encoding]::new($false))
        $doc.Close(0);$doc=$null
        Copy-Item -LiteralPath $cleanPath -Destination $root -Force
        [PSCustomObject]@{CleanPages=$cleanPages;CleanInlineImages=$cleanFigures;FieldsUpdated=$true;ContentsUpdated=$true} | ConvertTo-Json | Set-Content -LiteralPath "$root\qa\word_verification.json" -Encoding UTF8
        Write-Output "Prepared clean report: $cleanPages pages, $cleanFigures inline images."
        return
    }
    Write-Output 'Exporting PDF.'
    $doc.ExportAsFixedFormat($pdfPath,17)
    $cleanText=$doc.Content.Text
    $cleanPages=$doc.ComputeStatistics(2)
    $cleanFigures=$doc.InlineShapes.Count
    [System.IO.File]::WriteAllText("$root\qa\clean_word_text.txt",$cleanText,[Text.UTF8Encoding]::new($false))
    Write-Output "Clean report rendered: $cleanPages pages, $cleanFigures inline images."
    foreach ($path in @($cleanPath,$pdfPath)) {Copy-Item -LiteralPath $path -Destination $root -Force}
    if ($SkipComparison) {
        [PSCustomObject]@{CleanPages=$cleanPages;CleanInlineImages=$cleanFigures;Comparison='pending'} | ConvertTo-Json | Set-Content -LiteralPath "$root\qa\word_verification.json" -Encoding UTF8
        return
    }

    Write-Output 'Opening source for comparison.'
    $original=$word.Documents.Open($sourcePath,$false,$true)
    $sourceText=$original.Content.Text
    if ($original.Comments.Count -gt 0) {$original.DeleteAllComments()}
    Write-Output 'Comparing documents.'
    $comparison=$word.CompareDocuments($original,$doc,2,1,$false,$true,$true,$true,$true,$true,$true,$true,$false,$false,'Report revision',$true)
    $comparison.ShowRevisions=$true
    $comparison.TrackRevisions=$true
    $revisionCount=$comparison.Revisions.Count
    $comparison.SaveAs2($trackedPath,16)
    $comparison.Close(0);$comparison=$null
    $original.Close(0);$original=$null
    $doc.Close(0);$doc=$null

    # Acceptance/rejection checks operate on in-memory read-only opens.
    $comparison=$word.Documents.Open($trackedPath,$false,$true)
    $comparison.AcceptAllRevisions()
    $accepted=$comparison.Content.Text
    $acceptedExact=($accepted -ceq $cleanText)
    [System.IO.File]::WriteAllText("$root\qa\tracked_accepted_text.txt",$accepted,[Text.UTF8Encoding]::new($false))
    $comparison.Close(0);$comparison=$null
    $comparison=$word.Documents.Open($trackedPath,$false,$true)
    $comparison.RejectAllRevisions()
    $rejected=$comparison.Content.Text
    $rejectedExact=($rejected -ceq $sourceText)
    [System.IO.File]::WriteAllText("$root\qa\tracked_rejected_text.txt",$rejected,[Text.UTF8Encoding]::new($false))
    [System.IO.File]::WriteAllText("$root\qa\original_word_text.txt",$sourceText,[Text.UTF8Encoding]::new($false))
    $comparison.Close(0);$comparison=$null
    foreach ($path in @($cleanPath,$pdfPath,$trackedPath)) {Copy-Item -LiteralPath $path -Destination $root -Force}
    [PSCustomObject]@{
        CleanPages=$cleanPages; CleanInlineImages=$cleanFigures; WordRevisionCount=$revisionCount;
        AcceptedTextExact=$acceptedExact; RejectedTextExact=$rejectedExact;
        CleanDOCX="$root\Framework_revised_20261028.docx";
        PDF="$root\Framework_revised_20261028.pdf";
        TrackedDOCX="$root\Framework_revised_20261028_tracked.docx"
    } | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath "$root\qa\word_verification.json" -Encoding UTF8
    Write-Output "Tracked comparison: $revisionCount revisions; accept exact=$acceptedExact; reject exact=$rejectedExact"
}
finally {
    if ($null -ne $comparison) {$comparison.Close(0)}
    if ($null -ne $original) {$original.Close(0)}
    if ($null -ne $doc) {$doc.Close(0)}
    if ($null -ne $word) {$word.Quit()}
}
