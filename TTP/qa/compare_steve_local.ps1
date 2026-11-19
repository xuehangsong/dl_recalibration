$ErrorActionPreference='Stop'
$root='\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\TTP'
$source=Join-Path $root 'TTP_FY27Update_Recalibration of Deep Learning Models_steve.docx'
$clean=Join-Path $root 'TTP_FY27Update_Recalibration_Song_20261106_v2.docx'
$output=Join-Path $root 'TTP_FY27Update_Recalibration_Song_20261106_tracked_from_Steve.docx'
$temp=Join-Path $env:TEMP ('recalibration_compare_'+[guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $temp | Out-Null
Copy-Item -LiteralPath $source -Destination (Join-Path $temp 'steve.docx')
Copy-Item -LiteralPath $clean -Destination (Join-Path $temp 'revised.docx')
$delivery=$output
$source=Join-Path $temp 'steve.docx'
$clean=Join-Path $temp 'revised.docx'
$output=Join-Path $temp 'tracked.docx'
Write-Output 'Temporary inputs ready.'
$word=$null;$original=$null;$revised=$null;$comparison=$null
try {
 $word=New-Object -ComObject Word.Application
 Write-Output 'Word started.'
 $word.Visible=$false;$word.DisplayAlerts=0
 $original=$word.Documents.Open($source,$false,$true)
 # Steve's accepted proposal is the comparison baseline; his source is never saved.
 Write-Output 'Steve document opened.'
 $original.AcceptAllRevisions()
 $original.TrackRevisions=$false
 $baseline=$original.Content.Text
 $revised=$word.Documents.Open($clean,$false,$true)
 $target=$revised.Content.Text
 Write-Output 'Revised document opened.'
 $comparison=$word.CompareDocuments($original,$revised,2,1,$false,$true,$true,$true,$true,$true,$true,$true,$false,$false,'Song, Xuehang',$true)
 $comparison.TrackRevisions=$true;$comparison.ShowRevisions=$true
 $count=$comparison.Revisions.Count
 Write-Output "Comparison made: $count revisions."
 if($count -eq 0){throw 'No revisions generated'}
 $comparison.SaveAs2($output,16)
 $comparison.Close(0);$comparison=$null
 $comparison=$word.Documents.Open($output,$false,$true)
 $comparison.AcceptAllRevisions()
 $accept=($comparison.Content.Text -ceq $target)
 $comparison.Close(0);$comparison=$null
 $comparison=$word.Documents.Open($output,$false,$true)
 $comparison.RejectAllRevisions()
 $reject=($comparison.Content.Text -ceq $baseline)
 [PSCustomObject]@{Revisions=$count;AcceptMatchesRevised=$accept;RejectMatchesSteveAccepted=$reject;Baseline='Steve proposal with his existing revisions accepted in memory';Author='Song, Xuehang'} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $root 'qa\tracked_from_steve_verification.json') -Encoding UTF8
 if(-not $accept -or -not $reject){throw "Comparison mismatch accept=$accept reject=$reject"}
 Copy-Item -LiteralPath $output -Destination $delivery -Force
 Write-Output "Verified native Word comparison: $count revisions; accept matches revised text; reject restores Steve's proposed text."
}
finally {
 if($null -ne $comparison){$comparison.Close(0)}
 if($null -ne $revised){$revised.Close(0)}
 if($null -ne $original){$original.Close(0)}
 if($null -ne $word){$word.Quit()}
}
