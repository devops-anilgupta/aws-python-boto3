#!/bin/bash

######################################################
# auto-complete-shell-script.sh - [Github Copilot Auto-Complete Shell Script by ChatGPT seeing comments]

# Description: Create VPC in AWS
# - Create VPC
# - Create Subnet

# - Verify if user has AWS Installed, User might be using windows, linux or mac
# - Verify if profile dev exists
######################################################

#variables
AWS_REGION="us-east-1"
VPC_NAME="demo-vpc"
SUBNET_NAME="demo-subnet"
CIDR_BLOCK="10.0.0.0/16"
SUBNET_CIDR_BLOCK="10.0.1.0/24"
SUBNET_AZ="us-east-1a"

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "AWS CLI is not installed. Please install it first."
    exit 1
fi

# Profile dev check
if ! aws configure list-profiles | grep -q "dev"; then
    echo "Profile 'dev' does not exist. Please create it using 'aws configure --profile dev'."
    exit 1
fi

# Verify if AWS CLI is configured
if ! aws sts get-caller-identity &> /dev/null; then
    echo "AWS CLI is not configured. Please configure it using 'aws configure'."
    exit 1
fi

# Create VPC
VPC_ID=$(aws ec2 create-vpc --cidr-block $CIDR_BLOCK --output text --query 'Vpc.VpcId')
if [ -z "$VPC_ID" ]; then
    echo "Failed to create VPC."
    exit 1
fi
echo "VPC created with ID: $VPC_ID"

# Tag the VPC
aws ec2 create-tags --resources $VPC_ID --tags Key=Name,Value=$ 
VPC_NAME
echo "VPC tagged with Name: $VPC_NAME"

# Create Subnet
SUBNET_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block $SUBNET_CIDR_BLOCK --availability-zone $SUBNET_AZ --output text --query 'Subnet.SubnetId')
if [ -z "$SUBNET_ID" ]; then
    echo "Failed to create Subnet."
    exit 1
fi
echo "Subnet created with ID: $SUBNET_ID"

# Tag the Subnet
aws ec2 create-tags --resources $SUBNET_ID --tags Key=Name,Value=$SUBNET_NAME
echo "Subnet tagged with Name: $SUBNET_NAME"
# Output the created resources
echo "Created VPC ID: $VPC_ID"
echo "Created Subnet ID: $SUBNET_ID"
echo "VPC Name: $VPC_NAME"
echo "Subnet Name: $SUBNET_NAME"
echo "Script completed successfully."
exit 0
######################################################
# End of script
######################################################
# Note: Ensure you have the necessary permissions to create VPC and Subnet in your AWS account.
#       This script assumes you have the AWS CLI configured with appropriate credentials.
#       Modify the AWS_REGION variable if you want to create resources in a different region.
#       You can run this script on any Unix-like system with bash and AWS CLI installed.
######################################################
# Usage: Save this script as auto-complete-shell-script.sh and run it using bash.
# Example: bash auto-complete-shell-script.sh
######################################################
# Ensure you have the necessary permissions to create VPC and Subnet in your AWS account.
# This script assumes you have the AWS CLI configured with appropriate credentials.
# Modify the AWS_REGION variable if you want to create resources in a different region.
# You can run this script on any Unix-like system with bash and AWS CLI installed.
# Usage: Save this script as auto-complete-shell-script.sh and run it using bash.
# Example: bash auto-complete-shell-script.sh
######################################################
# Ensure you have the necessary permissions to create VPC and Subnet in your AWS account.
# This script assumes you have the AWS CLI configured with appropriate credentials.
# Modify the AWS_REGION variable if you want to create resources in a different region.         