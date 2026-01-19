import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("portfolio-visitor-counter")

def lambda_handler(event, context):
    response = table.update_item(
        Key={"id": "home"},
        UpdateExpression="SET #c = if_not_exists(#c, :zero) + :inc",
        ExpressionAttributeNames={"#c": "count"},
        ExpressionAttributeValues={":inc": 1, ":zero": 0},
        ReturnValues="UPDATED_NEW"
    )

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "count": response["Attributes"]["count"]
        })
    }
