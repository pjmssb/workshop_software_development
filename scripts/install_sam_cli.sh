#!/bin/bash

# Set the script to exit immediately if a command exits with a non-zero status
set -e

# Function to check if SAM CLI is installed
check_sam_cli_installed() {
    # Try to get the version of SAM CLI, if it's installed
    if command -v sam &> /dev/null; then
        return 0
    else
        return 1
    fi
}

# Function to install SAM CLI
install_sam_cli() {
    # Check if pip is installed
    if ! command -v pip &> /dev/null; then
        echo "pip is not installed. Installing pip..."
        curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
        python get-pip.py
        rm get-pip.py
        echo "pip installed successfully."
    fi

    # Now, use pip to install SAM CLI
    if pip install aws-sam-cli; then
        echo "SAM CLI installed successfully."
    else
        echo "Error occurred while installing SAM CLI."
        exit 1
    fi
}

# Main script logic

# Check if SAM CLI is already installed
if ! check_sam_cli_installed; then
    install_sam_cli
else
    echo "SAM CLI is already installed."
fi

