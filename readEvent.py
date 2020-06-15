import boto3
import json
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

def handle(event, context):
    print('hello world')
    dynamodb = boto3.resource('dynamodb', endpoint_url="https://dynamodb.eu-central-1.amazonaws.com")

    table = dynamodb.Table('events')

    print("event: {}".format(event))
    print("event: {}".format(event['requestContext']))

    try:
        #response = table.get_item(Key={'event'})
        
        last_evaluated_key = None
        response = table.scan()
        
        print("event: {}".format(response['Items']))

        #return response['Items']
        return {
            "statusCode": 200,
            'headers' : {
                'Access-Control-Allow-Origin' : '*'
            },
            "body": json.dumps(response['Items'])
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


