import boto3
from boto3.dynamodb.conditions import Key

from src.exception.dynamodb_integration_exception import DynamodbIntegrationException


def get_connection_dynamodb():
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4569", region_name="sa-east-1", aws_access_key_id="admin", aws_secret_access_key="admin")
    return dynamodb.Table('ocr-cupom')


class OcrCupomRepository:

    def __init__(self):
        self.connection = get_connection_dynamodb()

    def find_by_status(self, status_param):
        try:
            data = self.connection.query(KeyConditionExpression='status_cupom = :status_param',
                             ExpressionAttributeValues={':status_param': str(status_param)})

            return data['Items']
        except Exception as error:
            raise DynamodbIntegrationException("Error ao criar registro do cupom no DynamoDB")