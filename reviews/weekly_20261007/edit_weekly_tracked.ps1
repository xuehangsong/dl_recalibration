$ErrorActionPreference = 'Stop'
$root = '\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\reviews\weekly_20261007'
$source = "$root\source.docx"
$output = 'C:\Users\song884\OneDrive - PNNL\Desktop\PNNL_EM-HQ-TOO_WeeklyHighlight_DeepLearningModels_10_7_26_Xuehang_tracked.docx'
$auditPath = "$root\verification.json"
$previewPath = "$root\accepted_preview.pdf"

# Each edit targets only the exact changed words in the original draft.
$edits = @(
    @{Context='first-generation multimodal AI framework'; Old='multimodal AI'; New='deep-learning recalibration'},
    @{Context='This self-calibrating framework'; Old='self-calibrating '; New=''},
    @{Context='framework enables rapid, low-cost updates'; Old='enables'; New='is designed to support'},
    @{Context='framework enables rapid, low-cost updates'; Old='rapid, low-cost '; New=''},
    @{Context='data, improving predictive fidelity'; Old='improving'; New='with the aim of improving'},
    @{Context='from validated technical capability toward a documented, governance-ready decision-support tool'; Old='from validated technical capability toward a documented, governance-ready decision-support tool'; New='and its supporting documentation'},
    @{Context='first-generation multimodal AI framework that integrates'; Old='that integrates'; New='(Figure 1) that integrates'},
    @{Context='several notable milestones (Figure 1):'; Old=' (Figure 1)'; New=''},
    @{Context='helping ensure the surrogate performs well on both historical'; Old='ensure the surrogate performs well on both'; New='assess performance tradeoffs between'},
    @{Context='rare, high-consequence conditions'; Old=', high-consequence'; New=''},
    @{Context='conditions rather than favoring one at the expense of the other'; Old=' rather than favoring one at the expense of the other'; New=''},
    @{Context='evidence developed this year'; Old='this year'; New='during FY26'},
    @{Context='science-defensible predictive modeling'; Old='science-defensible'; New='scientifically defensible'},
    @{Context='can continuously evolve with incoming site data'; Old='continuously evolve'; New='be updated'},
    @{Context='formalized governance workflow'; Old='formalized'; New='documented'},
    @{Context='High-level workflow illustrating'; Old='High-level'; New='Conceptual'},
    @{Context='Once trained using high-performance computing'; Old=' using high-performance computing'; New=''},
    @{Context='two feedback pathways maintain long-term reliability'; Old='two'; New='three'},
    @{Context='two feedback pathways maintain long-term reliability'; Old='maintain long-term reliability'; New='support model updating'},
    @{Context='recalibration of the deep-learning model using targeted updates'; Old=''; New='recalibration of the physics-based numerical model, '}
)
$comments = @(
    @{Anchor='first-generation'; Text='I adjusted the maturity wording to distinguish the framework design and adaptive-replay experiments from operational deployment. "Multimodal" could imply data-modality fusion; "deep-learning recalibration" describes the scope documented in the Task 1 report.'},
    @{Anchor='Superior Paper Award'; Text='Please confirm the official award title and when the selection was announced, so its inclusion among developments since May is accurate.'},
    @{Anchor='Figure 1.'; Text='The figure shows three feedback paths: conceptual site model update, numerical-model recalibration, and surrogate recalibration. I aligned the caption. Please also change "Physical-based Numerical model" to "Physics-based Numerical Model" in the source figure.'}
)

$word = $null
$doc = $null
try {
    if (Test-Path -LiteralPath $output) { throw 'Output already exists; preserve for review.' }
    $sourceHash = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $word.DisplayAlerts = 0
    $priorName = $word.UserName
    $priorInitials = $word.UserInitials
    $word.UserName = 'Xuehang Song'
    $word.UserInitials = 'XS'
    $doc = $word.Documents.Open($source, $false, $true)
    if ($doc.Revisions.Count -ne 0 -or $doc.Comments.Count -ne 0) { throw 'Source contains review markup; inspect before continuing.' }
    $original = $doc.Content.Text
    $paragraphCount = $doc.Paragraphs.Count
    $inlineCount = $doc.InlineShapes.Count
    $shapeCount = $doc.Shapes.Count
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
    foreach ($comment in $comments) {
        $range = $doc.Content.Duplicate
        $find = $range.Find
        $find.ClearFormatting()
        $find.Text = $comment.Anchor
        $find.Forward = $true
        $find.Wrap = 0
        $find.MatchCase = $true
        $find.MatchWildcards = $false
        if (-not $find.Execute()) { throw "Missing comment anchor: $($comment.Anchor)" }
        [void]$doc.Comments.Add($range, $comment.Text)
    }
    $doc.Save()
    $doc.Close(0)
    $doc = $null

    # Test both review outcomes in memory, leaving saved markup intact.
    $doc = $word.Documents.Open($output, $false, $true)
    $revisionCount = $doc.Revisions.Count
    $commentCount = $doc.Comments.Count
    if ($commentCount -ne $comments.Count) { throw 'Unexpected comment count' }
    $revisionSpans = @()
    foreach ($rev in $doc.Revisions) {
        if ($rev.Range.Text.Contains("`r")) { throw 'A revision crosses a paragraph boundary' }
        $revisionSpans += [PSCustomObject]@{Type=[int]$rev.Type; Author=$rev.Author; Text=$rev.Range.Text}
    }
    $doc.AcceptAllRevisions()
    if ($doc.Content.Text -cne $expected) { throw 'Accepted text does not match planned edits' }
    if ($doc.Paragraphs.Count -ne $paragraphCount) { throw 'Paragraph structure changed' }
    if ($doc.InlineShapes.Count -ne $inlineCount -or $doc.Shapes.Count -ne $shapeCount) { throw 'Figure count changed' }
    $doc.DeleteAllComments()
    $doc.TrackRevisions = $false
    $doc.ShowRevisions = $false
    $doc.Repaginate()
    $pageCount = $doc.ComputeStatistics(2)
    $doc.ExportAsFixedFormat($previewPath, 17)
    $doc.Close(0)
    $doc = $word.Documents.Open($output, $false, $true)
    $doc.RejectAllRevisions()
    if ($doc.Content.Text -cne $original) { throw 'Rejected text does not restore source' }
    $doc.Close(0)
    $doc = $null
    if ((Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash -cne $sourceHash) { throw 'Source hash changed' }
    [PSCustomObject]@{
        Output=$output; SourceSHA256=$sourceHash; TargetedEdits=$edits.Count;
        WordRevisionCount=$revisionCount; CommentCount=$commentCount; ParagraphCount=$paragraphCount;
        AcceptedTextMatches=$true; RejectedTextMatchesOriginal=$true; FigureCountUnchanged=$true;
        SourceUnchanged=$true; Revisions=$revisionSpans; AcceptedText=$expected;
        Comments=$comments; PreviewPDF=$previewPath; AcceptedPageCount=$pageCount
    } | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $auditPath -Encoding UTF8
    Write-Output "VERIFIED: $($edits.Count) targeted edits; $revisionCount Word revisions; $commentCount comments; $pageCount preview pages; accepted/rejected text and figure count verified."
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
