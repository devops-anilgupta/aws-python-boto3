import boto3
import datetime
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

# Lambda function to check idle EC2 instances based on CPU utilization
def check_idle_ec2(event=None, context=None):
    ec2 = boto3.client('ec2')
    cloudwatch = boto3.client('cloudwatch')

    try:
        instances = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )

        idle_instances = []

        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']

                end_time = datetime.datetime.utcnow()
                start_time = end_time - datetime.timedelta(minutes=5)

                metrics = cloudwatch.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName='CPUUtilization',
                    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                    StartTime=start_time,
                    EndTime=end_time,
                    Period=60,
                    Statistics=['Average']
                )

                datapoints = metrics.get('Datapoints', [])
                avg_cpu = (
                    sum(dp['Average'] for dp in datapoints) / len(datapoints)
                    if datapoints else 0
                )

                avg_cpu = round(avg_cpu, 2)
                log.info(f"Instance {instance_id} - Avg CPU: {avg_cpu}%")

                if avg_cpu < 5:
                    idle_instances.append((instance_id, avg_cpu))

        log.info(f"[RESULT] Idle EC2 Instances (last 5 mins): {idle_instances}")
        return {"idle_instances": idle_instances}

    except Exception as e:
        log.error(str(e))
        return {"error": str(e)}
    
if __name__ == "__main__":
    check_idle_ec2()

