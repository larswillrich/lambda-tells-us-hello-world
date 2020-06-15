import boto3
import json

def handle(event, context):
    dynamodb = boto3.resource('dynamodb', endpoint_url="https://dynamodb.eu-central-1.amazonaws.com")

    table = dynamodb.Table('events')

    body = json.loads(event['body'])
    print("event: {}".format(body))

    response = table.put_item(Item = body)

    print("response: {}".format(response))

    return {
        "statusCode": 200,
        'headers' : {
            'Access-Control-Allow-Origin' : '*'
        },
        "body": json.dumps(body)
    }


