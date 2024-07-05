import json
import boto3

def lambda_handler(event, context):
    # CloudTrailからのログデータを取得
    for record in event['Records']:
        s3_bucket = record['s3']['bucket']['name']
        s3_key = record['s3']['object']['key']
        
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
        log_data = response['Body'].read().decode('utf-8')
        
        # ログデータを解析
        log_events = json.loads(log_data)
        for log_event in log_events['Records']:
            event_name = log_event['eventName']
            user_identity = log_event['userIdentity']
            
            # 特定のイベントに対してアラートを設定
            if event_name == 'ConsoleLogin' and user_identity['type'] == 'Root':
                send_alert(log_event)
                
    return {
        'statusCode': 200,
        'body': json.dumps('Log processed successfully')
    }

def send_alert(log_event):
    sns = boto3.client('sns')
    message = f"Alert: Root user login detected. Details: {json.dumps(log_event)}"
    sns.publish(
        TopicArn='arn:aws:sns:region:account-id:security-alerts',
        Message=message,
        Subject='Security Alert: Root User Login'
    )
