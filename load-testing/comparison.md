# Postman load-test comparison

Both runs used 10 virtual users, a 2-minute ramp-up load profile, the same `list` request shape, and the same API route. CloudWatch confirms the initial Lambda memory was **128 MB** and the updated memory was **1024 MB**.

| Metric | Baseline (128 MB) | Updated (1024 MB) |
|---|---:|---:|
| Total requests | 489 | 594 |
| Throughput (requests/s) | 3.88 | 4.70 |
| Mean latency | 353 ms | 108 ms |
| p90 | 371 ms | 113 ms |
| p95 | 404 ms | 148 ms |
| p99 | 2,855 ms | 274 ms |
| Minimum | 263 ms | 73 ms |
| Maximum | 3,945 ms | 1,802 ms |
| Reported errors | 0% | 0% |

**Calculations:** Mean latency reduction = `(353 − 108) / 353 × 100 = 69.4%`. Throughput increase = `(4.70 − 3.88) / 3.88 × 100 = 21.1%`. Request count increased by 105 (21.5%).

## Interpretation

The updated configuration had lower observed latency and higher throughput in these runs. AWS Lambda's CPU allocation scales with configured memory, which is a plausible mechanism. However, this was not a randomized or repeated controlled trial: the timeout was also increased, and DynamoDB latency, cold starts, background load, and data volume were not isolated. **Do not claim the entire improvement was caused by memory alone.**

A separate 128 MB CloudWatch `REPORT` example shows a timeout after 3,000 ms. That example may have occurred outside the Postman test windows and therefore does not contradict the reports' 0% error rates. It should not be averaged against the successful 1024 MB log entry.

## Better follow-up experiment

Run at least three repeats per configuration, alternate test order, hold timeout and dataset constant, capture API Gateway and Lambda latency distributions, and note cold-start frequency. Include Lambda duration and billed duration separately from API latency; compare total cost per successful request, not only speed.
