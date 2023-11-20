# install_python.ps1

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
        Write-Host "Python is not installed."
        return $false
    }
}

# Function to check if pip is installed
function CheckPipInstalled {
    try {
        $pipVersion = $(pip --version) 2>&1
        if ($pipVersion -like "pip*") {
            return $true
        } else {
            return $false
        }
    } catch {
        Write-Host "pip is not installed."
        return $false
    }
}

# Function to install Python
function InstallPython {
    try {
        # Download the Python installer
        $installerPath = "$env:TEMP\python_installer.exe"
        Invoke-WebRequest -Uri "https://www.python.org/ftp/python/latest/python-3.9.7-amd64.exe" -OutFile $installerPath

        # Install Python
        Start-Process -Wait -FilePath $installerPath -ArgumentList "/passive", "InstallAllUsers=1", "PrependPath=1", "Include_test=0"

        # Remove the installer
        Remove-Item -Path $installerPath -Force

        Write-Host "Python installed successfully."
    } catch {
        Write-Error "Error during Python installation: $_"
        exit 1
    }
}

# Function to install pip
function InstallPip {
    try {
        # Install pip using Python's ensurepip module
        python -m ensurepip --upgrade

        Write-Host "pip installed successfully."
    } catch {
        Write-Error "Error during pip installation: $_"
        exit 1
    }
}

# Main script logic

# Check and install Python
if (-not (CheckPythonInstalled)) {
    InstallPython
} else {
    Write-Host "Python is already installed."
}

# Check and install pip
if (-not (CheckPipInstalled)) {
    InstallPip
} else {
    Write-Host "pip is already installed."
}

