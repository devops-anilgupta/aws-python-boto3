# Goal: Find and delete old files (>30 days) in an S3 bucket.
import boto3
import datetime

BUCKET_NAME = 'your-s3-bucket-name'

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    deleted_files = []
    now = datetime.datetime.utcnow()

    objects = s3.list_objects_v2(Bucket=BUCKET_NAME)
    for obj in objects.get('Contents', []):
        last_modified = obj['LastModified'].replace(tzinfo=None)
        age = (now - last_modified).days
        if age > 30:
            s3.delete_object(Bucket=BUCKET_NAME, Key=obj['Key'])
            deleted_files.append(obj['Key'])

    print(f"Deleted {len(deleted_files)} old files.")
    return {"deleted": deleted_files}
