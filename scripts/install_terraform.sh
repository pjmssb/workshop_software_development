#!/bin/bash

# Set the script to exit immediately if a command exits with a non-zero status
set -e

# Function to check if Terraform is installed
check_terraform_installed() {
    if command -v terraform &> /dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to install Terraform
install_terraform() {
    # Downloading the Terraform binary
    TEMP_DIR=$(mktemp -d)
    TERRAFORM_URL="https://releases.hashicorp.com/terraform/1.1.2/terraform_1.1.2_linux_amd64.zip"
    
    curl -o "$TEMP_DIR/terraform.zip" "$TERRAFORM_URL"
    unzip "$TEMP_DIR/terraform.zip" -d "$TEMP_DIR"
    sudo mv "$TEMP_DIR/terraform" /usr/local/bin/
    rm -rf "$TEMP_DIR"
}

# Main script logic

if ! check_terraform_installed; then
    echo "Installing Terraform..."
    install_terraform
else
    echo "Terraform is already installed."
fi

