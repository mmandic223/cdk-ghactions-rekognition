#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from aws_cdk import (
    Environment,
    App
)

from github_stack.github_stack import AwsGithubActionsPolicyStack
load_dotenv()

environment = os.getenv('ENVIRONMENT')
app_name = os.getenv('APP_NAME')


app = App()

AwsGithubActionsPolicyStack(app,'{0}-stack-github'.format(environment),
            env=Environment(account=os.getenv('AWS_ACCOUNT'),
                            region=os.getenv('AWS_REGION')))

app.synth()
