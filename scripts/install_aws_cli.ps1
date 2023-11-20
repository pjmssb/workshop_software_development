# install_aws_cli.ps1

# Ensure any errors stop script execution
$ErrorActionPreference = "Stop"

# Function to check if AWS CLI is installed
function CheckAWSCLIInstalled {
    try {
        # Attempt to get AWS CLI version
        $awsVersion = $(aws --version) 2>$null
        if (-not $awsVersion) {
            return $false
        } else {
            return $true
        }
    } catch {
        Write-Host "Error while checking AWS CLI installation."
        return $false
    }
}

# Function to download and install AWS CLI
function InstallAWSCLI {
    try {
        # Download AWS CLI MSI installer
        $installerPath = "$env:TEMP\AWSCLIV2.msi"
        Invoke-WebRequest -Uri "https://awscli.amazonaws.com/AWSCLIV2.msi" -OutFile $installerPath

        # Install AWS CLI using the MSI installer
        Start-Process -Wait -FilePath msiexec -ArgumentList "/i $installerPath"

        # Provide feedback on successful installation
        Write-Host "AWS CLI installed successfully."
    } catch {
        # Handle any exceptions during installation
        Write-Error "Error during AWS CLI installation: $_"
        exit 1
    }
}

# Main script logic

# Check if AWS CLI is already installed
if (-not (CheckAWSCLIInstalled)) {
    InstallAWSCLI
} else {
    Write-Host "AWS CLI is already installed."
}

# Prompt user to configure the AWS CLI
try {
    Read-Host "Press Enter to configure the AWS CLI"
    aws configure
} catch {
    Write-Error "Error during AWS CLI configuration: $_"
}
