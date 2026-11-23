# Key learnings and limitations

1. **Memory is also a compute-performance control.** Lambda memory sizing can change allocated CPU and therefore latency, not just memory headroom.
2. **Function-level and API-level measurements answer different questions.** Power Tuning's duration/cost is not interchangeable with Postman's HTTP response time.
3. **The cheapest invocation is not always the smallest memory setting.** Power Tuning selected 1024 MB for this specific cost-oriented workload.
4. **A single timed-out invocation is not a benchmark.** Cold starts, timeout thresholds, and the lack of matched sampling make individual log entries unsuitable for estimating the overall speedup.
5. **Measured association is not causation.** Two sequential runs, even with verified memory settings, cannot isolate all sources of latency variation.
6. **Publish evidence safely.** Use placeholder ARNs and URLs; never publish tokens, secrets, or a live unauthenticated API endpoint.

## Next iteration

Repeat load tests at all four memory levels, hold timeout constant, record Lambda and DynamoDB CloudWatch metrics, report cost per successful API request, and capture confidence intervals across repeated runs.
