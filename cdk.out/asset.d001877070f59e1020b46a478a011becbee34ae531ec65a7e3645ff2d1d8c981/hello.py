from base64 import decode
import email
import json
import uuid

GET_RAW_PATH = "/getPerson"
CREATE_RAW_PATH = "/createPerson"

def handler(event, context):
    print(event)
    if event['path'] == GET_RAW_PATH:
        print ("Start Request for GetPerson")
        personId = event['queryStringParameters']['personId']
        print ("Received request with PersonID = " + personId)
        return {"firstName": "Tasib", "lastName": "Ali", "email": "tasib@yaoo.com"}

    elif event['path'] == CREATE_RAW_PATH:
        print ("Start Request for CREATE_Person")
        decodeEvent = json.loads(event['body'])
        firstName = decodeEvent['firstName']
        print ("Received request with firstName = " + firstName)
        return {"personId": str(uuid.uuid1())}

