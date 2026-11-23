# Lambda configuration screenshots

- `lambda-general-configuration.png`: final memory **1024 MB**, timeout **5 seconds**, ephemeral storage **512 MB**, SnapStart **None**.
- `lambda-runtime-settings.png`: **Python 3.15**, handler **`lambda_function.lambda_handler`**, architecture **x86_64**.

These screenshots document the **final** state only. The initial 128 MB memory is verified by the sanitized CloudWatch log excerpt in `results/`. Initial runtime and architecture were confirmed by the experimenter; an original configuration screenshot is not available.
