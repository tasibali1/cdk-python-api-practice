
def handler(event, context):
    try:
        first_num = event["queryStringParameters"]['firstNum']
    except KeyError:
        first_num = 0

    try:
        second_num = event["queryStringParameters"]['secondNum']
    except KeyError:
        second_num = 0

    try:
        third_num = event["queryStringParameters"]['thirdNum']
    except KeyError:
        third_num = 0

    try:
        fourth_num = event["queryStringParameters"]['fourthNum']
    except KeyError:
        fourth_num = 0

    try:
        fifth_num = event["queryStringParameters"]['fifthNum']
    except KeyError:
        fifth_num = 0

    result = int(first_num) + int(second_num) + int(third_num) + int(fourth_num) + int(fifth_num)
    print("The result of % s + % s + % s + % s + % s = %s" % (first_num, second_num, third_num, fourth_num, fifth_num, result))
    return {'body': result, 'statusCode': 200}




