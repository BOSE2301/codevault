import boto3
from botocore.exceptions import NoCredentialsError

# AWS S3 bucket name
BUCKET_NAME = 'sandipproject'
FILE_NAME = 'weather.csv'

def upload_to_s3(file_name, bucket_name):
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, file_name)
        print(f'Successfully uploaded {file_name} to {bucket_name}')
    except FileNotFoundError:
        print(f'The file {file_name} was not found')
    except NoCredentialsError:
        print('Credentials not available')

if __name__ == "__main__":
    upload_to_s3(FILE_NAME, BUCKET_NAME)