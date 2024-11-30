import json

def lambda_handler(event, context):
    # TODO implement
    display_welcome_message()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! ahhh')
    }

# Welcome message
def display_welcome_message():

    print("""
    ************************************************************
    *              Welcome to the Email Extractor              *
    *     Please wait while we process your URLs               *
    ************************************************************
    """)