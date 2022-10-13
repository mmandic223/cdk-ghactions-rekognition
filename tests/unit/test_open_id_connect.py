import aws_cdk as core
import aws_cdk.assertions as assertions
from dotenv import load_dotenv
import os
from github_provider.github_stack.github_stack import AwsGithubActionsPolicyStack

load_dotenv()

environment = os.getenv('ENVIRONMENT')
app_name = os.getenv('APP_NAME')

def test_github_provider():
    app = core.App()
    stack = AwsGithubActionsPolicyStack(app, '{0}-stack-rekognition'.format(environment),)
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("Custom::AWSCDKOpenIdConnectProvider", {
        "Url": "https://token.actions.githubusercontent.com"
    })

def test_github_oidc_role_created():
    app = core.App()
    stack = AwsGithubActionsPolicyStack(app, '{0}-stack-rekognition'.format(environment),)
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::IAM::Role", {
        "AssumeRolePolicyDocument": {
            "Statement": [{
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                }
            }]
        } 
    })
