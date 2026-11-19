$ErrorActionPreference = 'Stop'
$source = '\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\reviews\q4_fy26\source.docx'
$output = 'C:\Users\song884\OneDrive - PNNL\Desktop\Q4 Status Report Draft_Xuehang_tracked.docx'
$auditPath = '\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\reviews\q4_fy26\verification.json'

# Anchor each change in its original context; track only the selected words.
$edits = @(
    @{Context='manuscript consolidation'; Old='consolidation'; New='revision'},
    @{Context='securing project continuity'; Old='securing'; New='planning for'},
    @{Context='securing project continuity'; Old='continuity'; New='completion'},
    @{Context='requested and fully approved'; Old='fully '; New=''},
    @{Context='communicating project maturity'; Old='maturity'; New='status'},
    @{Context='the full seven-step'; Old='full'; New='proposed'},
    @{Context='provided deeper insight'; Old='deeper '; New=''},
    @{Context='convergence behavior, performance tradeoffs'; Old=', '; New=' and '},
    @{Context='performance tradeoffs, and the conditions required to achieve balanced accuracy across both historical'; Old=', and the conditions required to achieve balanced accuracy across both'; New=' between'},
    @{Context='historical and extreme data regimes'; Old='extreme'; New='rare'},
    @{Context='Manuscript Nearing Completion:'; Old='Nearing Completion'; New='Revisions'},
    @{Context='including resolution of reviewer-style comments'; Old='resolution of'; New='responses to'},
    @{Context='including resolution of reviewer-style comments'; Old='reviewer-style'; New='internal review'},
    @{Context='operational relevance'; Old=''; New='potential '},
    @{Context='operational relevance of the framework'; Old='the framework'; New='adaptive replay'},
    @{Context='is positioned for submission'; Old='positioned'; New='being prepared'},
    @{Context='consolidating all model performance'; Old='all '; New=''},
    @{Context='a comprehensive technical summary'; Old='comprehensive '; New=''},
    @{Context='Secured No-Cost Time Extension and Structured Remaining Work:'; Old='Secured No-Cost Time Extension and '; New=''},
    @{Context='maximize focused effort on deliverable completion'; Old='maximize focused effort on'; New='allow more time for'}
)

$word = $null
$doc = $null
try {
    if (Test-Path -LiteralPath $output) {
        if (-not (Test-Path -LiteralPath $auditPath)) { throw 'Existing output has no verification record' }
        $priorAudit = Get-Content -Raw -LiteralPath $auditPath | ConvertFrom-Json
        if ($priorAudit.Output -cne $output -or -not $priorAudit.AcceptedTextMatches) { throw 'Unrecognized output' }
    }
    $sourceHash = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $priorName = $word.UserName
    $priorInitials = $word.UserInitials
    $word.UserName = 'Xuehang Song'
    $word.UserInitials = 'XS'
    $doc = $word.Documents.Open($source, $false, $true)
    if ($doc.Revisions.Count -ne 0) { throw 'Source contains existing revisions; review before proceeding.' }
    $original = $doc.Content.Text
    $paragraphCount = $doc.Paragraphs.Count
    $changes = @()
    foreach ($edit in $edits) {
        $pos = $original.IndexOf($edit.Context, [StringComparison]::Ordinal)
        if ($pos -lt 0) { throw "Missing context: $($edit.Context)" }
        if ($original.IndexOf($edit.Context, $pos + 1, [StringComparison]::Ordinal) -ge 0) { throw "Ambiguous context: $($edit.Context)" }
        $offset = $edit.Context.IndexOf($edit.Old, [StringComparison]::Ordinal)
        if ($offset -lt 0) { throw 'Missing edit within context' }
        $changes += [PSCustomObject]@{Start=($pos+$offset); Old=$edit.Old; New=$edit.New}
    }
    $changes = @($changes | Sort-Object Start -Descending)
    $expected = $original
    $previousStart = $original.Length
    foreach ($change in $changes) {
        if (($change.Start + $change.Old.Length) -gt $previousStart) { throw 'Overlapping edits' }
        $expected = $expected.Remove($change.Start, $change.Old.Length).Insert($change.Start, $change.New)
        $previousStart = $change.Start
    }
    $doc.SaveAs2($output, 16)
    $doc.TrackRevisions = $true
    $doc.ShowRevisions = $true
    foreach ($change in $changes) {
        $range = $doc.Range($change.Start, $change.Start + $change.Old.Length)
        if ([string]$range.Text -cne $change.Old) { throw "Range mismatch for $($change.Old)" }
        if ($change.New.Length -eq 0) { [void]$range.Delete() } else { $range.Text = $change.New }
    }
    $doc.Save()
    $doc.Close(0)
    $doc = $null

    # Test both review outcomes in memory, leaving the saved revisions intact.
    $doc = $word.Documents.Open($output, $false, $true)
    $revisionCount = $doc.Revisions.Count
    $revisionSpans = @()
    foreach ($rev in $doc.Revisions) {
        $revisionSpans += [PSCustomObject]@{Type=[int]$rev.Type; Author=$rev.Author; Text=$rev.Range.Text}
    }
    $doc.AcceptAllRevisions()
    if ($doc.Content.Text -cne $expected) { throw 'Accepted text does not match planned edits' }
    if ($doc.Paragraphs.Count -ne $paragraphCount) { throw 'Paragraph structure changed' }
    $doc.Close(0)
    $doc = $word.Documents.Open($output, $false, $true)
    $doc.RejectAllRevisions()
    if ($doc.Content.Text -cne $original) { throw 'Rejected text does not restore source' }
    $doc.Close(0)
    $doc = $null
    if ((Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash -cne $sourceHash) { throw 'Source hash changed' }
    [PSCustomObject]@{
        Output=$output; SourceSHA256=$sourceHash; TargetedEdits=$edits.Count;
        WordRevisionCount=$revisionCount; ParagraphCount=$paragraphCount;
        AcceptedTextMatches=$true; RejectedTextMatchesOriginal=$true;
        SourceUnchanged=$true; Revisions=$revisionSpans; AcceptedText=$expected
    } | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $auditPath -Encoding UTF8
    Write-Output "VERIFIED: $($edits.Count) targeted edits; $revisionCount Word revisions; accepted/rejected text verified; source unchanged."
    Write-Output $output
}
finally {
    if ($null -ne $doc) { $doc.Close(0) }
    if ($null -ne $word) {
        if ($null -ne $priorName) { $word.UserName = $priorName }
        if ($null -ne $priorInitials) { $word.UserInitials = $priorInitials }
        $word.Quit()
    }
}
