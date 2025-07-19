import boto3
import datetime
import json
import os

ssm = boto3.client('ssm')
cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

PARAM_NAME = os.environ.get('SSM_PARAM_NAME')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

def get_instance_ids():
    try:
        response = ssm.get_parameter(Name=PARAM_NAME)
        return json.loads(response['Parameter']['Value'])
    except Exception as e:
        print(f"SSM read failed: {e}")
        return []

def lambda_handler(event, context):
    instance_ids = get_instance_ids()
    now = datetime.datetime.utcnow()
    start_time = now - datetime.timedelta(hours=12)
    
    summary = f"🕓 Monitoring Summary ({start_time} to {now} UTC)\n\n"
    
    for instance_id in instance_ids:
        data = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
            StartTime=start_time,
            EndTime=now,
            Period=3600,
            Statistics=['Average']
        )
        points = data.get('Datapoints', [])
        avg_cpu = sum(p['Average'] for p in points) / len(points) if points else 0
        summary += f"EC2 {instance_id}: Avg CPU = {avg_cpu:.2f}%\n"

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="📊 Daily Monitoring Summary",
        Message=summary
    )
