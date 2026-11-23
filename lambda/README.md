# Illustrative Lambda function

This is **new example code**, not the original benchmarked workshop function. It permits only read-only scans of the DynamoDB table named by the `TABLE_NAME` environment variable. It caps returned items at 1,000 and uses scan pagination. The actual workshop function accepted additional operations and returned a different response shape, so its measured timings **must not** be attributed to this example.

For production, prefer query operations with indexed access patterns, request authentication, careful pagination and response-size limits, and a tightly scoped IAM policy granting `dynamodb:Scan` only for the intended test table. Do not deploy publicly without authorization.
