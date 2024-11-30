import json
import boto3
import base64
import datetime

def lambda_handler(event, context):
    display_welcome_message()
    uploadFileToS3(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Job started')
    }

def uploadFileToS3(event):
    S3 = boto3.client("s3")
    get_file_content = event["content"]
    decode_content = base64.b64decode(get_file_content)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    S3.put_object(Bucket="python-test-170278925856/input",Key="data" + str(timestamp)+ ".csv",Body=decode_content)

# Welcome message
def display_welcome_message():

    print("""
    ************************************************************
    *              Welcome to the Email Extractor              *
    *     Please wait while we process your URLs               *
    ************************************************************
    """)