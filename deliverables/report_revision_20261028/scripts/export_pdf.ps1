$ErrorActionPreference='Stop'
$root='\\wsl.localhost\Ubuntu\home\song884\github\dl_recalibration\deliverables\report_revision_20261028'
$tempRoot=Join-Path $env:LOCALAPPDATA 'Temp\dl_report_revision_20261028'
$docPath=Join-Path $tempRoot 'Framework_revised_20261028.docx'
$target="$root\qa\pdf_export_target.pdf"
$word=$null;$doc=$null
try {
 $word=New-Object -ComObject Word.Application
 $word.Visible=$false;$word.DisplayAlerts=0
 $doc=$word.Documents.Open($docPath,$false,$true)
 Write-Output 'Exporting existing Word-verified document to existing PDF target.'
 $doc.ExportAsFixedFormat($target,17)
 Write-Output 'PDF export finished.'
 Copy-Item -LiteralPath $target -Destination "$root\Framework_revised_20261028.pdf" -Force
 [PSCustomObject]@{Pages=$doc.ComputeStatistics(2);Exporter='Microsoft Word';Source=$docPath} | ConvertTo-Json | Set-Content -LiteralPath "$root\qa\pdf_export_verification.json" -Encoding UTF8
}
finally {if($null -ne $doc){$doc.Close(0)};if($null -ne $word){$word.Quit()}}
