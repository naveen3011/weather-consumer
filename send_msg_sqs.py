import boto3
import json

def send_message_to_sqs():
   
    queue_url = 'https://sqs.us-east-1.amazonaws.com/054244991161/weatherQueue'

    # Message to be sent
    weather_info = {
        "coord": {"lon": 77.0299, "lat": 28.4646},
        "weather": [{"id": 701, "main": "Mist", "description": "mist", "icon": "50n"}],
        "base": "stations",
        "main": {"temp": 9.02, "feels_like": 9.02, "temp_min": 8.93, "temp_max": 9.02, "pressure": 1016, "humidity": 93},
        "visibility": 1000,
        "wind": {"speed": 0, "deg": 0},
        "clouds": {"all": 74},
        "dt": 1705346070,
        "sys": {"type": 1, "id": 9165, "country": "IN", "sunrise": 1705369514, "sunset": 1705407420},
        "timezone": 19800,
        "id": 1270642,
        "name": "Gurugram",
        "cod": 200
    }


    sqs = boto3.client('sqs',region_name='us-east-1')

    # Send the message to the SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(weather_info)
    )

    print(f"Message sent. MessageId: {response['MessageId']}")


send_message_to_sqs()
