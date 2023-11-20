# install_terraform.ps1

# Ensure any errors stop script execution
$ErrorActionPreference = "Stop"

# Function to check if Terraform is installed
function CheckTerraformInstalled {
    try {
        $terraformVersion = $(terraform -v)
        if ($terraformVersion -like "Terraform v*") {
            return $true
        } else {
            return $false
        }
    } catch {
        Write-Host "Terraform not installed."
        return $false
    }
}

# Function to install Terraform
function InstallTerraform {
    # Using Chocolatey to install Terraform
    choco install terraform
}

# Main script logic

if (-not (CheckTerraformInstalled)) {
    Write-Host "Installing Terraform..."
    InstallTerraform
} else {
    Write-Host "Terraform is already installed."
}

