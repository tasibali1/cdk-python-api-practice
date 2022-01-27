
def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    if event['path'] == "/":
        a=1
        b=2
        c = a + b 
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
            },
            'body': 'Good Day, Tasib! You have hit {} \n'.format(c)
        }

