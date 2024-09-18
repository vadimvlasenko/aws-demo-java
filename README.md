# Hello API CDK Python Project

This project contains a Python CDK stack that defines an API Gateway with a `/hello` endpoint connected to a Lambda function.

## Prerequisites

- AWS CLI configured with appropriate permissions
- AWS CDK installed (`npm install -g aws-cdk`)
- Python 3.8 installed

## Project Structure

```plaintext
├── README.md
├── app.py
├── cdk.json
├── lambda/
│   └── hello_world.py
├── requirements.txt
├── setup.py
├── source.bat
├── source.sh
├── hello_api/
│   ├── __init__.py
│   ├── hello_api_stack.py
└── .github/
    └── workflows/
        └── ci-cd.yaml
```

## Deploying the Stack

To deploy the stack, run:

```sh
cdk deploy
```

## GitHub Actions CI/CD

This project includes a GitHub Actions workflow for continuous integration and deployment. The workflow is defined in `.github/workflows/ci-cd.yaml`.

### Secrets

Ensure the following secrets are added to your GitHub repository:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

## Cleaning Up

To delete the deployed resources, run:

```sh
cdk destroy
```
