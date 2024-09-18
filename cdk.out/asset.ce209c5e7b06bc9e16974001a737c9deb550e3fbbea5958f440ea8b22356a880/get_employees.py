import json

def handler(event, context):
    employees = [
        {"id": 1, "name": "DHONI"},
        {"id": 2, "name": "KHOLI"}
    ]
    return {
        'statusCode': 200,
        'body': json.dumps(employees)
    }
