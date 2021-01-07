import boto3


s3_client = boto3.resource('s3')
s3.meta.client.upload_file()


