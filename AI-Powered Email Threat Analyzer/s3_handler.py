import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
def upload_to_s3(aws_access_key, aws_secret_key, bucket_name, file_content, object_name):
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    try:
        s3_client.put_object(Body=file_content, Bucket=bucket_name, Key=object_name)
        return f"Successfully uploaded to S3 bucket '{bucket_name}' as {object_name}"
    except (NoCredentialsError, PartialCredentialsError): return "S3 Upload Failed: AWS credentials are not valid."
    except Exception as e: return f"S3 Upload Failed: {e}"
