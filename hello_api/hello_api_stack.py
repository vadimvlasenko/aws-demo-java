from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    Environment
)
import os
from constructs import Construct

class HelloApiStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        env = Environment(
            account=os.environ["CDK_DEFAULT_ACCOUNT"],
            region=os.environ["CDK_DEFAULT_REGION"]
        )
        super().__init__(scope, id, env=env, **kwargs)

        # Define the Lambda function
        hello_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello_world.handler',
        )

        # Define the API Gateway
        api = apigw.LambdaRestApi(
            self, 'HelloApi',
            handler=hello_lambda,
            proxy=False
        )

        # Define the /hello endpoint
        hello = api.root.add_resource('hello')
        hello.add_method('GET')
