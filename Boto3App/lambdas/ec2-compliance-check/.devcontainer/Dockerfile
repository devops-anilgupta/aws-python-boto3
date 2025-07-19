FROM python:3.12-slim

# ✅ Install Docker CLI + SAM CLI manually
RUN apt update && \
    apt install -y docker.io curl unzip less && \
    apt clean

# ✅ Install AWS SAM CLI manually (optional)
RUN curl -Lo sam.zip https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip && \
    unzip sam.zip -d sam-installation && \
    ./sam-installation/install && \
    rm -rf sam.zip sam-installation
