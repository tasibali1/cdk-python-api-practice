from base64 import decode
import email
import json
import uuid
import requests


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    
    # URL = "https://w6he7cwsg3.execute-api.eu-west-1.amazonaws.com/prod/"
    # API_KEY = "some_api_key"
    
    # data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # r = requests.post(URL, data=json.dumps(data), headers=headers)
    # print(r.status_code)
    # print(r.json())

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
        firstName = 'firstName'
        print("Received request with firstName = " + firstName)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body':  'personId: {} \n' .format( str(uuid.uuid1()) )
    }

    if (event['path'] == '/path/to/resource'):
        print ("Start Request for CREATE_Person")
        decodeEvent = json.loads(event['body'])
        firstName = decodeEvent['firstName']
        print("Received request with firstName = " + firstName)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body':  'personId: {} \n' .format( str(uuid.uuid1()) )
    }

