import boto3
import json
import os

sns = boto3.client('sns')

ALLOWED_TYPES = [t.strip() for t in os.environ['ALLOWED_TYPES'].split(',')]
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))
    
    invoking_event = json.loads(event['invokingEvent'])
    configuration_item = invoking_event.get('configurationItem')
    
    if not configuration_item:
        print("No configuration item found.")
        return build_response('NOT_APPLICABLE', 'No configuration item to evaluate.')

    instance_id = configuration_item['resourceId']
    instance_type = configuration_item['configuration']['instanceType']
    environment = configuration_item['tags'].get('Environment', 'Unknown')

    if instance_type not in ALLOWED_TYPES:
        message = (
            f"❌ NON-COMPLIANT EC2 Instance Detected\n"
            f"Environment: {environment}\n"
            f"Instance ID: {instance_id}\n"
            f"Instance Type: {instance_type}\n"
            f"Allowed Types: {', '.join(ALLOWED_TYPES)}"
        )
        print(message)
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="🚨 EC2 Instance Type Compliance Violation",
            Message=message
        )
        return build_response('NON_COMPLIANT', f"{instance_type} is not an allowed EC2 instance type.")
    
    print(f"✅ Instance {instance_id} of type {instance_type} is compliant.")
    return build_response('COMPLIANT', f"{instance_type} is an allowed EC2 instance type.")

def build_response(compliance_type, annotation):
    return {
        'compliance_type': compliance_type,
        'annotation': annotation
    }
