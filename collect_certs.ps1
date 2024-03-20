param (
    [string]$SourceDirectory,
    [string]$OutputDirectory
)

# Check if source directory exists
if (-not (Test-Path $SourceDirectory -PathType Container)) {
    Write-Host "Source directory '$SourceDirectory' does not exist or is not a directory."
    exit 1
}

# Check if output directory exists, create it if not
if (-not (Test-Path $OutputDirectory -PathType Container)) {
    Write-Host "Creating output directory '$OutputDirectory'..."
    New-Item -Path $OutputDirectory -ItemType Directory | Out-Null
}

# Iterate through files in source directory
foreach ($file in Get-ChildItem -Path $SourceDirectory -Filter *.exe) {
    $cert = Get-PfxCertificate -FilePath $file.FullName -NoPrompt
    if ($cert) {
        $certPem = $cert.Export([System.Security.Cryptography.X509Certificates.X509ContentType]::Cert)
        $certPemPath = Join-Path -Path $OutputDirectory -ChildPath ($file.BaseName + ".pem")
        Set-Content -Path $certPemPath -Value $certPem -Encoding UTF8
        Write-Host "Certificate extracted from $($file.Name) and saved as $($certPemPath)"
    }
    else {
        Write-Host "Failed to extract certificate from $($file.Name)"
    }
}
