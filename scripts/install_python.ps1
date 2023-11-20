# install_upgrade_python.ps1

# Ensure any errors stop script execution
$ErrorActionPreference = "Stop"

# Function to check if Python is installed
function CheckPythonInstalled {
    try {
        $pythonVersion = $(python --version) 2>&1
        if ($pythonVersion -like "Python*") {
            return $true
        } else {
            return $false
        }
    } catch {
        Write-Host "Error while checking Python installation."
        return $false
    }
}

# Function to install/upgrade Python
function InstallUpgradePython {
    # NOTE: This script assumes Chocolatey is installed on Windows to manage packages.
    # Install Python
    choco install python --force

    # Upgrade pip
    python -m pip install --upgrade pip
}

# Main script logic

# Check if Python is already installed
if (-not (CheckPythonInstalled)) {
    Write-Host "Installing Python..."
} else {
    Write-Host "Upgrading Python to the latest version..."
}

InstallUpgradePython
Write-Host "Python and pip are now on their latest versions."

