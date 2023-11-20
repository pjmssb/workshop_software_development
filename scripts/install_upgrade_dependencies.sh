#!/bin/bash

# Set the script to exit immediately if a command exits with a non-zero status
set -e

# Define the path to requirements.txt
REQUIREMENTS_PATH="../requirements.txt"

# Check if requirements.txt exists
if [[ ! -f $REQUIREMENTS_PATH ]]; then
    echo "requirements.txt not found in the parent directory."
    exit 1
fi

# Function to install/upgrade Python dependencies
install_upgrade_dependencies() {
    pip install --upgrade pip
    pip install -r $REQUIREMENTS_PATH
}

# Main script logic
install_upgrade_dependencies
echo "Dependencies installed/upgraded successfully."

