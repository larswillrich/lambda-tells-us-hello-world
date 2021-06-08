import json
import boto3
from botocore.exceptions import ClientError

def handle(event, context):
    print('hello world, I am the first log entry')

    print("event: {}".format(event))
    print("event: {}".format(event['requestContext']))

    try:

        if event['multiValueQueryStringParameters'] is None:
            name = ''
        elif "name" in event['multiValueQueryStringParameters']:
            name = ", {}".format(event['multiValueQueryStringParameters']["name"][0])
        else:
            name = ''

        return {
            "statusCode": 200,
            'headers' : {
                'Access-Control-Allow-Origin' : '*'
            },
            "body": "Hello World" + name
            }
    except ClientError as e:
        print(e.response['Error']['Message'])

    #print("response: {}".format(response))

    return {
        "statusCode": 300,
        'headers' : {
            'Access-Control-Allow-Origin' : '*'
        },
        "body": 'error'
    }


