#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_cdk import (
    Environment,
    App
)
from dotenv import load_dotenv

# config = load_dotenv(".env")
# environment = config['ENV']


from stacks.cdk_app_stack import BussinesLogicStack
from stacks.github_connection_stack import GithubConnection


app = cdk.App()
BussinesLogicStack(app,'dev-stack-rekognition',
            env=Environment(account=os.getenv('AWS_ACCOUNT'),
                            region=os.getenv('AWS_REGION')))

GithubConnection(app,'dev-environment-stack-githubconnection',
            env=Environment(account=os.getenv('AWS_ACCOUNT'),
                            region=os.getenv('AWS_REGION')))


app.synth()
