# Install required tools:
sudo apt-get update && sudo apt-get install -y unzip curl python3-pip

#  Download and Install SAM CLI
curl -Lo sam-installation.zip https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
unzip sam-installation.zip -d sam-installation
sudo ./sam-installation/install

# Verify Installation
sam --version


