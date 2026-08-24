import boto3

target_region = "ap-south-1"
client = boto3.client('s3', region_name= target_region)

response = client.get_bucket_acl(
    Bucket='rittik-python-bucket',
    ExpectedBucketOwner='631421280316'
)
print(response)