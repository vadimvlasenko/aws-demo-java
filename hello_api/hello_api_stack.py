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

        # Define the Lambda function for /hello
        hello_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello_world.handler',
        )

        # Define the Lambda function for GET /employees
        get_employees_lambda = _lambda.Function(
            self, 'GetEmployeesHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda'),
            handler='get_employees.handler',
        )

        # Define the Lambda function for POST /employee
        post_employee_lambda = _lambda.Function(
            self, 'PostEmployeeHandler',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.from_asset('lambda'),
            handler='post_employee.handler',
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

        # Define the /employees endpoint
        employees = api.root.add_resource('employees')
        employees.add_method('GET', apigw.LambdaIntegration(get_employees_lambda))

        # Define the /employee endpoint
        employee = api.root.add_resource('employee')
        employee.add_method('POST', apigw.LambdaIntegration(post_employee_lambda))
