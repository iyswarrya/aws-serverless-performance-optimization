# Implementation and reproduction notes

## Components

- **API Gateway:** HTTPS POST route `/Prod/DynamoDBManager` (the public collection replaces the live hostname with a variable).
- **Lambda:** Python 3.15, x86_64, handler `lambda_function.lambda_handler`; initial memory 128 MB, updated memory 1024 MB.
- **DynamoDB:** A test table named `lambda-apigateway` in the recorded experiment; the `list` operation performs a scan.
- **CloudWatch Logs:** `REPORT` entries for memory settings, durations, and timeout status.
- **Step Functions / Power Tuning:** Runs repeated invocations across memory configurations and returns a recommendation.
- **Postman:** Measures the client-observed end-to-end request/response path under concurrent load.

## Request body

```json
{"operation":"list","tableName":"lambda-apigateway","payload":{}}
```

## Running the Postman collection

Import the collection JSON and set `baseUrl` to `https://YOUR_API_ID.execute-api.us-west-2.amazonaws.com` (do not include `/Prod/DynamoDBManager`). Configure the runner to use Performance → Ramp up → 10 virtual users → 2 minutes, where supported by your Postman version. Test a private, authorized endpoint only.

## Reproduction caveat

The sample in `lambda/` is a **safer illustrative implementation**, intentionally not the exact code used during the measured workshop run. It restricts operations to read-only `list`, requires an explicitly configured table name, and paginates the scan. Because this differs from the original implementation, do **not** present performance results from the workshop as measurements of this sample code. To reproduce the historical benchmark exactly, the original code and infrastructure would need to be independently verified and restored in a safe test environment.

## Teardown

Disable or delete test API endpoints and unused Lambda, DynamoDB, and Step Functions resources after testing; review billing and IAM access.
