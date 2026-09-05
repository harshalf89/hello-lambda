"""A minimal AWS Lambda function.

AWS calls `lambda_handler` every time the function runs.
- `event` holds the input (whatever triggered it / whatever you pass in).
- `context` holds runtime info (request id, time left, etc.).
Whatever you return becomes the function's output.
"""


def lambda_handler(event, context):
    name = event.get("name", "world") if isinstance(event, dict) else "world"
    return {
        "statusCode": 200,
        "body": f"Hello, {name}! This ran on AWS Lambda.",
    }
