# LLM Bot Scripts Documentation

This document provides an overview of various utility scripts included in the `llm_bot/scripts` directory. These scripts are designed to set up and manage the development environment for the LLM Bot project, ensuring that contributors can easily install, configure, and manage necessary dependencies.

## Prerequisites

- Ensure you have the appropriate command-line environment:
    - PowerShell for Windows
    - Bash for Linux/macOS
- Administrative or superuser rights may be required for certain tasks.
- For PowerShell scripts, execution policy might need to be modified to allow script execution (use `Set-ExecutionPolicy` cmdlet for this).

## Scripts

### install_aws_cli.ps1 / install_aws_cli.sh

- **Purpose**: Checks if AWS CLI is installed, installs it if absent, or updates to the latest version if it's outdated.
- **Usage**:
    - PowerShell: `.\install_aws_cli.ps1`
    - Bash: `./install_aws_cli.sh`

### install_sam_cli.ps1 / install_sam_cli.sh

- **Purpose**: Checks if AWS SAM CLI is installed, installs it if absent, or updates to the latest version if it's outdated.
- **Usage**:
    - PowerShell: `.\install_sam_cli.ps1`
    - Bash: `./install_sam_cli.sh`

### install_upgrade_python.ps1 / install_upgrade_python.sh

- **Purpose**: Ensures Python and pip are installed and upgrades them to the latest available versions.
- **Usage**:
    - PowerShell: `.\install_upgrade_python.ps1`
    - Bash: `./install_upgrade_python.sh`

### install_upgrade_dependencies.ps1 / install_upgrade_dependencies.sh

- **Purpose**: Installs and upgrades the Python dependencies listed in the `requirements.txt` file located in the parent directory.
- **Usage**:
    - PowerShell: `.\install_upgrade_dependencies.ps1`
    - Bash: `./install_upgrade_dependencies.sh`

**Note**: Before running the scripts, navigate to the `llm_bot/scripts` directory in your command-line environment. For PowerShell scripts on Windows, you may need to run your PowerShell session with elevated privileges (Run as Administrator).

## Contributing

Ensure that you test any changes by running the scripts in a clean environment before submitting a pull request. Additionally, please update this README if you add new scripts or modify the existing ones' functionality.

For any issues, feature requests, or contributions, please submit a request through the project's issue tracker.

---
Happy coding!
