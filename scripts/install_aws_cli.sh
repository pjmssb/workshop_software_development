#!/bin/bash

# Set the script to exit immediately if a command exits with a non-zero status
set -e

# Function to check if AWS CLI is installed
check_aws_cli_installed() {
    if command -v aws &> /dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to download and install AWS CLI
install_aws_cli() {
    # Download AWS CLI installer
    local installer_file="awscliv2.zip"

    if curl -o "$installer_file" "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip"; then
        echo "Downloaded the AWS CLI installer successfully."

        # Extract and install
        unzip "$installer_file"
        sudo ./aws/install

        # Cleanup
        rm -f "$installer_file"
        rm -rf ./aws

        echo "AWS CLI installed successfully."
    else
        echo "Error while downloading the AWS CLI installer."
        exit 1
    fi
}

# Main script logic

# Check if AWS CLI is already installed
if ! check_aws_cli_installed; then
    install_aws_cli
else
    echo "AWS CLI is already installed."
fi

# Prompt user to configure the AWS CLI
read -p "Press Enter to configure the AWS CLI" 
aws configure || {
    echo "Error during AWS CLI configuration."
    exit 1
}
