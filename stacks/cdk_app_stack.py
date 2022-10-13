
from aws_cdk import (
    CfnOutput, Duration, RemovalPolicy, Stack,
    aws_ec2 as _ec2,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_logs as log,
    aws_s3 as s3,
    aws_s3_notifications as s3_notify,
)

from constructs import Construct
from dotenv import dotenv_values

class BussinesLogicStack(Stack):

    def __init__(self, scope: Construct, construct_id: str,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        config = dotenv_values(".env")
        # Parameters from .env

        environment = config['ENV']
        first_name_last_name = config['FIRST_LAST_NAME']


        # GET Method Lambda

        lambda_func = _lambda.Function(self, 
                                           'lambda_api_get_func',
                                           runtime=_lambda.Runtime.PYTHON_3_9,
                                           function_name=f"{environment}-{first_name_last_name}-recognition",
                                           code=_lambda.AssetCode("./Functions"),
                                           handler='lambda_rekognition.lambda_handler'
                                    )

        # GET Method Lambda LG

        lambda_lg = log.LogGroup(self, 
                                      "lambda_mm_loggroup_get",
                                      log_group_name=f"/aws/lambda/{lambda_func.function_name}",
                                      removal_policy=RemovalPolicy.DESTROY,
                                )
        
        lambda_permission = iam.PolicyStatement(
            actions=['rekognition:*', 's3:*'],
            resources=['*']
        )

        lambda_func.role.attach_inline_policy(
            iam.Policy(self, 'rekognition-access', statements=[lambda_permission])
        )

        # S3 Bucket

        bucket = s3.Bucket(self, 'rekognition-bucket')

        
        # Create trigger for Lambda function using suffix

        notification = s3_notify.LambdaDestination(lambda_func)
        notification.bind(self, bucket)


        # Add Create Event only for .jpg files
        
        bucket.add_object_created_notification(
           notification, s3.NotificationKeyFilter(suffix='.jpg'))