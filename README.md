# hello-lambda

A tiny AWS Lambda function, deployed automatically by GitHub Actions on every push to `main`.

## Files

| File | Purpose |
|------|---------|
| `lambda_function.py` | The function code. Entry point: `lambda_function.lambda_handler` |
| `.github/workflows/deploy.yml` | CI pipeline: zips the code and pushes it to Lambda |

## Local test (no AWS needed)

```bash
python -c "import lambda_function; print(lambda_function.lambda_handler({'name': 'harshal'}, None))"
```

## AWS details

- Region: `us-east-1`
- Function name: `hello-lambda`
- Runtime: Python 3.12
