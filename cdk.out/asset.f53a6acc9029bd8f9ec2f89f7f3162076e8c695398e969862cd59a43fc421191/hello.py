from base64 import decode
import email
import json
import uuid


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    
    if (event['path'] == '/tasib'):
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': 'Good Day, Tasib! You have hit {} \n'.format(event['path'])
        }

    if (event['path'] == '/test1'):
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': 'You have hit {} \n'.format(event['path'])
        }

    if (event['path'] == '/postman'):
        print ("Start Request for CREATE_Person")
        decodeEvent = json.loads(event['body'])
        firstName = decodeEvent['firstName']
        print("Received request with firstName = " + firstName)
        return {"personId": str(uuid.uuid1())}

