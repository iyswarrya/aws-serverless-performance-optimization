# CloudWatch diagnostic excerpts

Sanitized excerpts from two supplied `REPORT` entries. Request IDs have been removed because they do not improve the public analysis.

**128 MB invocation**

```text
REPORT RequestId: <REQUEST_ID>  Duration: 3000.00 ms  Billed Duration: 3785 ms  Memory Size: 128 MB  Max Memory Used: 93 MB  Init Duration: 784.25 ms  Status: timeout
```

**1024 MB invocation**

```text
REPORT RequestId: <REQUEST_ID>  Duration: 37.72 ms  Billed Duration: 38 ms  Memory Size: 1024 MB  Max Memory Used: 100 MB
```

The first invocation timed out and included initialization overhead. The second completed without a reported error and did not show an initialization duration. **They are diagnostic examples, not a controlled two-point speedup calculation.** The initial timeout configuration was not separately captured; 3 seconds is inferred from the timeout event. The final timeout setting of 5 seconds is visible in the configuration screenshot.
