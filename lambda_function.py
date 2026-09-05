"""A minimal AWS Lambda function.

AWS calls `lambda_handler` every time the function runs.
- `event` holds the input (whatever triggered it / whatever you pass in).
- `context` holds runtime info (request id, time left, etc.).
Whatever you return becomes the function's output.
"""

import os

APP_ENV = os.environ.get("APP_ENV", "local")


def lambda_handler(event, context):
    name = event.get("name", "world") if isinstance(event, dict) else "world"
    return {
        "statusCode": 200,
        "body": f"Hi {name}! This is release v2, promoted dev -> staging -> prod. [env: {APP_ENV}]",
    }
