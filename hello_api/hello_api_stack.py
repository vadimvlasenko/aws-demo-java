import os

from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
    Environment,
    IAspect,
    Aspects
)
from aws_cdk import aws_iam as iam
from constructs import Construct, IConstruct


class PermissionBoundaryAspect(IAspect):
    def __init__(self, permission_boundary_arn: str):
        self.permission_boundary_arn = permission_boundary_arn

    def visit(self, node: IConstruct):
        if isinstance(node, iam.Role):
            node.add_permission_boundary(iam.ManagedPolicy.from_managed_policy_arn(
                node, "PermissionBoundary", self.permission_boundary_arn))


class HelloApiStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        env = Environment(
            account=os.environ["CDK_DEFAULT_ACCOUNT"],
            region=os.environ["CDK_DEFAULT_REGION"]
        )
        super().__init__(scope, id, env=env, **kwargs)
        permission_boundary_arn = "arn:aws:iam::025066278959:policy/eo_role_boundary"
        Aspects.of(self).add(PermissionBoundaryAspect(permission_boundary_arn))
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