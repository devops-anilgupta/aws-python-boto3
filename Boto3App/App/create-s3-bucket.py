import boto3
import botocore.exceptions
import os

# Set AWS profile (optional if already exported)
os.environ['AWS_PROFILE'] = 'dev'

def create_s3_bucket(bucket_name, region='us-east-1'):
    try:
        if region == 'us-east-1':
            client = boto3.client('s3', region_name=region)
            response = client.create_bucket(Bucket=bucket_name)
        else:
            client = boto3.client('s3', region_name=region)
            response = client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )

        print(f"✅ Bucket '{bucket_name}' created successfully.")
    except botocore.exceptions.ClientError as error:
        print(f"❌ Failed to create bucket: {error.response['Error']['Message']}")

# Call the function with a globally unique bucket name
create_s3_bucket("my-dev-container-bucket-12345678", region="us-east-1")
