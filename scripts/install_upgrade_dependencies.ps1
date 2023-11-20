# install_upgrade_dependencies.ps1

# Ensure any errors stop script execution
$ErrorActionPreference = "Stop"

# Define the path to requirements.txt
$requirementsPath = "..\requirements.txt"

# Check if requirements.txt exists
if (-not (Test-Path $requirementsPath)) {
    Write-Error "requirements.txt not found in the parent directory."
    exit 1
}

# Function to install/upgrade Python dependencies
function InstallUpgradeDependencies {
    try {
        python -m pip install --upgrade pip
        python -m pip install -r $requirementsPath
    } catch {
        Write-Error "Failed to install/upgrade dependencies: $_"
        exit 1
    }
}

# Main script logic
InstallUpgradeDependencies
Write-Host "Dependencies installed/upgraded successfully."

