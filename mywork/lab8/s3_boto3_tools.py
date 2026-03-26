import sys
import os
import boto3

s3 = boto3.client("s3", region_name="us-east-1")

bucket = sys.argv[1]
file_name = sys.argv[2]

key = os.path.basename(file_name)

with open(file_name, "rb") as f:
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=f
    )

print("uploaded private file")
print("s3://" + bucket + "/" + key)

url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": bucket, "Key": key},
    ExpiresIn=60
)

print(url)
