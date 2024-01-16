import json
import boto3
from decimal import Decimal

dynamo_db = boto3.resource('dynamodb')
table = dynamo_db.Table('newWeatherTableName')

def process_sqs_message(event, context):
    try:
        records = event['Records']
        for record in records:
            body = json.loads(record['body'])
            print('incoming message from sqs: ', body)
            res = store_in_dynamodb(body)
            print('Suceesfully Stored in DynamoDB: ', res)
        return {'statusCode': 200, 'body': 'Message processed successfully'}
    
    except Exception as e:
        print('Error processing SQS message:', str(e))
        return {'statusCode': 500, 'body': 'Error processing message'}



def store_in_dynamodb(data):
    params = {
        'TableName': 'weather',
        'Item': {
            'dt': int(data['dt']),
            'name': data['name'],
            'temp': Decimal(str(data['main']['temp'])),  
            'weather_id': int(data['weather'][0]['id']),
            'wind_speed': Decimal(str(data['wind']['speed'])),  
            'wind_deg': Decimal(str(data['wind']['deg'])),
            'clouds': Decimal(str(data['clouds']['all'])),
            'country': data['sys']['country']
        }
    }
    res=table.put_item(Item=params['Item'])
    return res