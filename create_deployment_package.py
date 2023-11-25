import os
import shutil
import subprocess
import zipfile
import sys

# Define paths
src_dir = './src'
deployment_dir = './deployment'
deployment_zip = './deployment/lambda_deployment_package.zip'
requirements_file = './src/requirements.txt'  # Update if your requirements file is located elsewhere

# Create deployment directory if it doesn't exist
if not os.path.exists(deployment_dir):
    os.makedirs(deployment_dir)

# Install dependencies from requirements.txt into the deployment directory
if os.path.exists(requirements_file):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_file, '-t', deployment_dir])

# Copy source files to the deployment directory
for filename in os.listdir(src_dir):
    file_path = os.path.join(src_dir, filename)
    if os.path.isfile(file_path):
        shutil.copy(file_path, deployment_dir)

# Create a zip file of the deployment directory
with zipfile.ZipFile(deployment_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(deployment_dir):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(deployment_dir, '..')))

# Delete .py files from the deployment directory
for file in os.listdir(deployment_dir):
    if file.endswith('.py'):
        os.remove(os.path.join(deployment_dir, file))

print("Deployment package created at:", deployment_zip)
