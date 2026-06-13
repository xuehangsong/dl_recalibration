# PowerShell script to parse EndNote XML and convert to BibTeX
$content = Get-Content -Path 'literature/bib.xml' -Raw

# Find all unique records
$recordMatches = [regex]::Matches($content, '<record>(.*?)</record>', 'Singleline')

$uniqueRecords = @{}
foreach ($match in $recordMatches) {
    $recordXml = $match.Groups[1].Value
    if ($recordXml -match '<rec-number>(\d+)</rec-number>') {
        $recNum = $Matches[1]
        if (-not $uniqueRecords.ContainsKey($recNum)) {
            $uniqueRecords[$recNum] = $recordXml
        }
    }
}

Write-Host "Found $($uniqueRecords.Count) unique records"

# Function to extract field from XML
function Get-XmlField {
    param($xml, $pattern)
    if ($xml -match $pattern) {
        return $Matches[1].Trim()
    }
    return $null
}

# Function to extract authors
function Get-Authors {
    param($xml)
    $authors = @()
    $authorMatches = [regex]::Matches($xml, '<author>([^<]+)</author>')
    foreach ($m in $authorMatches) {
        $authors += $m.Groups[1].Value
    }
    return $authors -join ' and '
}

# Function to clean text for BibTeX
function Clean-BibText {
    param($text)
    if (-not $text) { return $null }
    $text = $text -replace '&amp;', '\&'
    $text = $text -replace '&', '\&'
    $text = $text -replace '<[^>]+>', ''
    $text = $text -replace '\s+', ' '
    return $text.Trim()
}

# Function to generate citation key
function Get-CitationKey {
    param($authors, $year)
    if (-not $authors -or -not $year) { return "Unknown$year" }
    $firstAuthor = ($authors -split ' and ')[0]
    # Extract last name
    if ($firstAuthor -match ',') {
        $lastName = ($firstAuthor -split ',')[0].Trim()
    } else {
        $parts = $firstAuthor -split '\s+'
        $lastName = $parts[-1]
    }
    # Clean special characters
    $lastName = $lastName -replace '[^a-zA-Z]', ''
    return "$lastName$year"
}

# Map ref-type to BibTeX entry type
$refTypeMap = @{
    'Journal Article' = 'article'
    'Book' = 'book'
    'Book Section' = 'incollection'
    'Report' = 'techreport'
    'Conference Proceedings' = 'inproceedings'
    'Thesis' = 'phdthesis'
    'Web Page' = 'misc'
}

# Track citation keys for duplicates
$citationKeys = @{}

# Process each record
$bibEntries = @()
$verificationTable = @()

foreach ($recNum in ($uniqueRecords.Keys | Sort-Object {[int]$_})) {
    $xml = $uniqueRecords[$recNum]
    
    # Extract fields
    $refTypeName = Get-XmlField $xml '<ref-type name="([^"]+)"'
    $title = Get-XmlField $xml '<title>([^<]+)</title>'
    $secondaryTitle = Get-XmlField $xml '<secondary-title>([^<]+)</secondary-title>'
    $year = Get-XmlField $xml '<year>(\d{4})</year>'
    $volume = Get-XmlField $xml '<volume>([^<]+)</volume>'
    $number = Get-XmlField $xml '<number>([^<]+)</number>'
    $pages = Get-XmlField $xml '<pages>([^<]+)</pages>'
    $publisher = Get-XmlField $xml '<publisher>([^<]+)</publisher>'
    $doi = Get-XmlField $xml '<electronic-resource-num>([^<]+)</electronic-resource-num>'
    $isbn = Get-XmlField $xml '<isbn>([^<]+)</isbn>'
    $url = Get-XmlField $xml '<url>([^<]+)</url>'
    $pubLocation = Get-XmlField $xml '<pub-location>([^<]+)</pub-location>'
    
    $authors = Get-Authors $xml
    
    # Clean fields
    $title = Clean-BibText $title
    $secondaryTitle = Clean-BibText $secondaryTitle
    $publisher = Clean-BibText $publisher
    
    # Get BibTeX type
    $bibType = $refTypeMap[$refTypeName]
    if (-not $bibType) { $bibType = 'misc' }
    
    # Generate citation key
    $baseKey = Get-CitationKey $authors $year
    $citationKey = $baseKey
    if ($citationKeys.ContainsKey($baseKey)) {
        $citationKeys[$baseKey]++
        $suffix = [char]([int][char]'a' + $citationKeys[$baseKey] - 1)
        $citationKey = "$baseKey$suffix"
    } else {
        $citationKeys[$baseKey] = 1
    }
    
    # Build BibTeX entry
    $entry = "@$bibType{$citationKey,`n"
    if ($authors) { $entry += "  author = {$authors},`n" }
    if ($title) { $entry += "  title = {$title},`n" }
    if ($year) { $entry += "  year = {$year},`n" }
    
    switch ($bibType) {
        'article' {
            if ($secondaryTitle) { $entry += "  journal = {$secondaryTitle},`n" }
            if ($volume) { $entry += "  volume = {$volume},`n" }
            if ($number) { $entry += "  number = {$number},`n" }
            if ($pages) { $entry += "  pages = {$pages},`n" }
        }
        'book' {
            if ($publisher) { $entry += "  publisher = {$publisher},`n" }
            if ($pubLocation) { $entry += "  address = {$pubLocation},`n" }
            if ($volume) { $entry += "  volume = {$volume},`n" }
        }
        'incollection' {
            if ($secondaryTitle) { $entry += "  booktitle = {$secondaryTitle},`n" }
            if ($publisher) { $entry += "  publisher = {$publisher},`n" }
            if ($pubLocation) { $entry += "  address = {$pubLocation},`n" }
            if ($pages) { $entry += "  pages = {$pages},`n" }
        }
        'techreport' {
            if ($publisher) { $entry += "  institution = {$publisher},`n" }
            if ($number) { $entry += "  number = {$number},`n" }
        }
        'inproceedings' {
            if ($secondaryTitle) { $entry += "  booktitle = {$secondaryTitle},`n" }
            if ($publisher) { $entry += "  publisher = {$publisher},`n" }
            if ($pages) { $entry += "  pages = {$pages},`n" }
        }
    }
    
    if ($doi) { $entry += "  doi = {$doi},`n" }
    if ($isbn) { $entry += "  isbn = {$isbn},`n" }
    if ($url -and -not $doi) { $entry += "  url = {$url},`n" }
    
    $entry += "}`n"
    $bibEntries += $entry
    
    # Add to verification table
    $verificationTable += [PSCustomObject]@{
        RecNum = $recNum
        CitationKey = $citationKey
        Authors = if ($authors.Length -gt 50) { $authors.Substring(0, 47) + '...' } else { $authors }
        Year = $year
        Title = if ($title.Length -gt 60) { $title.Substring(0, 57) + '...' } else { $title }
        Type = $bibType
        DOI = $doi
        HasDOI = if ($doi) { 'Yes' } else { 'No' }
    }
}

# Write BibTeX file
$bibContent = "% BibTeX file generated from EndNote XML`n"
$bibContent += "% Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`n"
$bibContent += "% Total entries: $($bibEntries.Count)`n`n"
$bibContent += $bibEntries -join "`n"

$bibContent | Out-File -FilePath 'literature/references.bib' -Encoding UTF8

Write-Host "`nBibTeX file written to literature/references.bib"
Write-Host "Total entries: $($bibEntries.Count)"

# Write verification table
$verificationTable | Format-Table -AutoSize | Out-String | Out-File -FilePath 'literature/verification_table.txt' -Encoding UTF8

Write-Host "Verification table written to literature/verification_table.txt"

# Output summary
Write-Host "`n=== SUMMARY ==="
Write-Host "Total unique records: $($uniqueRecords.Count)"
Write-Host "Records with DOI: $(($verificationTable | Where-Object { $_.HasDOI -eq 'Yes' }).Count)"
Write-Host "Records without DOI: $(($verificationTable | Where-Object { $_.HasDOI -eq 'No' }).Count)"
