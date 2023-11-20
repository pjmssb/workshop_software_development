# install_sam_cli.ps1

# Ensure any errors stop script execution
$ErrorActionPreference = "Stop"

# Function to check if SAM CLI is installed
function CheckSAMCLIInstalled {
    try {
        # Attempt to get SAM CLI version
        $samVersion = $(sam --version) 2>$null
        if (-not $samVersion) {
            return $false
        } else {
            return $true
        }
    } catch {
        Write-Host "Error while checking SAM CLI installation."
        return $false
    }
}

# Function to install SAM CLI
function InstallSAMCLI {
    try {
        # Use pip to install SAM CLI
        pip install aws-sam-cli

        # Provide feedback on successful installation
        Write-Host "SAM CLI installed successfully."
    } catch {
        # Handle any exceptions during installation
        Write-Error "Error during SAM CLI installation: $_"
        exit 1
    }
}

# Main script logic

# Check if SAM CLI is already installed
if (-not (CheckSAMCLIInstalled)) {
    InstallSAMCLI
} else {
    Write-Host "SAM CLI is already installed."
}

