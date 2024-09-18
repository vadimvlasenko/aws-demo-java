import json

def handler(event, context):
    body = json.loads(event['body'])
    new_employee = {
        "id": body['id'],
        "name": body['name']
    }
    # Here, you would typically insert the new employee into a database.
    # For this example, we'll just return the new employee data.
    return {
        'statusCode': 200,
        'body': json.dumps({
            "message": "SUCCESS",
            "employee": new_employee
        })
    }
