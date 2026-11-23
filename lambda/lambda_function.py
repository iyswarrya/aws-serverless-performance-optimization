"""Illustrative read-only Lambda for a test DynamoDB table.

NOT the exact function measured in the historical case study.
Deploy only in a secured test environment with least-privilege IAM.
"""
import os
import boto3

_dynamodb = boto3.resource("dynamodb")


def lambda_handler(event, context):
    if not isinstance(event, dict) or event.get("operation") != "list":
        return {"error": "Only the list operation is supported"}

    table_name = os.environ.get("TABLE_NAME")
    if not table_name:
        raise RuntimeError("TABLE_NAME must be configured")
    if event.get("tableName") not in (None, table_name):
        return {"error": "Requested table is not permitted"}

    table = _dynamodb.Table(table_name)
    items = []
    cursor = None
    while True:
        params = {"Limit": 100}
        if cursor:
            params["ExclusiveStartKey"] = cursor
        result = table.scan(**params)
        items.extend(result.get("Items", []))
        cursor = result.get("LastEvaluatedKey")
        if not cursor or len(items) >= 1000:
            break
    return {"items": items[:1000], "truncated": bool(cursor)}
