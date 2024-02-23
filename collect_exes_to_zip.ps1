# Define the directory to search for .exe files
$sourceDirectory = "C:\"

# Define the destination zip file
$zipFile = [Environment]::GetFolderPath("Desktop")

# Check if the source directory exists
if (-not (Test-Path -Path $sourceDirectory)) {
    Write-Host "Source directory does not exist: $sourceDirectory"
    exit
}

# Search for .exe files recursively in the source directory
$exeFiles = Get-ChildItem -Path $sourceDirectory -Recurse -Filter *.exe

# Check if any .exe files were found
if (-not $exeFiles) {
    Write-Host "No .exe files found in $sourceDirectory or its subdirectories."
    exit
}

# Create a new empty zip file
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zipArchive = [System.IO.Compression.ZipFile]::Open($zipFile, 'Create')

# Iterate through each .exe file found and add it to the zip archive
foreach ($file in $exeFiles) {
    $fileRelativePath = $file.FullName.Substring($sourceDirectory.Length + 1)
    $entry = $zipArchive.CreateEntry($fileRelativePath)
    $entryStream = $entry.Open()
    $fileStream = $file.OpenRead()
    $fileStream.CopyTo($entryStream)
    $entryStream.Close()
    $fileStream.Close()
}

# Close the zip archive
$zipArchive.Dispose()

Write-Host "All .exe files have been copied to $zipFile."


