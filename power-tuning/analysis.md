# Power Tuning analysis

The Step Functions tuning workflow tested four memory configurations (128/256/512/1024 MB) with 10 invocations each. The input requested the **cost** strategy. The output selected **1024 MB**, reporting duration **45.668333 ms** and cost **7.728 × 10⁻⁷ USD** per invocation (as represented by the tool).

The output separately reports **$0.00045** for state machine execution and **$0.0001461411** for Lambda invocations within the tuning workflow. These are workflow-related charges, not the recommended function's per-invocation cost. The sum of these two reported components is **$0.0005961411**; other charges are not assessed here.

[View the interactive visualization](https://lambda-power-tuning.show/#gAAAAQACAAQ=;miH8RNBRL0QpHGdDYKw2Qg==;bTKONiDdRTYhyAI2aXJPNQ==). The output JSON does **not** include per-memory raw duration/cost arrays, so no additional per-memory values are invented in this repository. For complete experimental reproducibility, archive the raw Step Functions invocation measurements if available.

The 45.67 ms duration is function-level and should not be compared directly to the 108 ms Postman end-to-end mean. The result is specific to this input payload, environment, and time.
