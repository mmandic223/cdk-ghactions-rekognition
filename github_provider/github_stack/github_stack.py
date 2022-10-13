from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_iam as iam,
    CfnOutput
)
from constructs import Construct

class AwsGithubActionsPolicyStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        github_provider = iam.OpenIdConnectProvider(self , "GithubProvider",
            url="https://token.actions.githubusercontent.com",
            client_ids=["sts.amazonaws.com"]    
        )

        CfnOutput(self, "GitHubProviderArn" , value=github_provider.open_id_connect_provider_arn)