import boto3

target_region = "ap-south-1"

client = boto3.client('s3', region_name=target_region)

response = client.create_bucket(
    Bucket='rittik-python-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': target_region
    }
)