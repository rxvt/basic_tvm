import json
import boto3


def get_client(service):
    client = boto3.client(service, region_name="us-east-1")
    return client


def assume_role(policy_document, account):
    client = get_client("sts")
    credentials = client.assume_role(
        RoleArn=f"arn:aws:iam::{account}:role/tvmtest",
        RoleSessionName="tvmtest",
        Policy=json.dumps(policy_document),
    )
    return credentials
