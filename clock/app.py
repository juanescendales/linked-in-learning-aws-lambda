import json
from datetime import datetime
from pytz import timezone
import time

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    zone = event["queryStringParameters"]["timezone"]
    fmt = "%Y-%m-%d %H:%M:%S %Z%z"
    now_time = datetime.now(timezone("UTC")) 
    
    if zone:
        now_time = now_time.astimezone(zone) 

    time.sleep(2)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f'Todays is : {now_time.strftime(fmt)}',
        }),
    }
