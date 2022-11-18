from aws_cdk import (
    # Duration,
    Stack,
    aws_s3_deployment,
    CfnOutput
)
from aws_solutions_constructs.aws_cloudfront_s3 import CloudFrontToS3
from constructs import Construct

class WebRepositoryStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        myWebSite = CloudFrontToS3(self, 'myWebRepo')

        aws_s3_deployment.BucketDeployment(self, "DeployIndexFile",
            sources=[aws_s3_deployment.Source.asset("./web")],
            destination_bucket=myWebSite.s3_bucket,            
        )
        
        CfnOutput(self, "indexURL", value="{}/index.html".format(myWebSite.cloud_front_web_distribution.distribution_domain_name))
