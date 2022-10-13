import boto3
from urllib.parse import unquote_plus
import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def detect(bucket,name):
    
    """
    Detects labels from images passed
    Core bussines logic
    """
    
    client = boto3.client("rekognition")
    
    response = client.detect_labels(
            Image = {"S3Object": {"Bucket": bucket, "Name": name}}
        )
    
    return response
    

def lambda_handler(event, context):
    
    """
    Computer vision lambda handler
    Prepares data for main bussines logic
    """
    
    logger.info(event)
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        
    my_labels = detect(bucket=bucket, name=key)
    
    
    return my_labels
    