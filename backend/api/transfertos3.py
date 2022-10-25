#util/transferToS3.py
import boto3
from botocore.client import Config
import datetime

s3Client = boto3.client('s3')

ACCESS_KEY_ID = '----------------'
ACCESS_SECRET_KEY = '-------------------------'
BUCKET_NAME = 'pod-icons'
REGION = 'us-west-2'
FOLDER = 'icons'

'''
#-commented code is under development or ignorable
'''

def create_presigned_urls(s3Client, bucket_name: str, key: str, expires_in: int):
    """
    \nCreates presigned_urls \n
    Args:
        s3Client (s3 Class): boto3 S3 Class
        bucket_name
        key
        expires_in: The number of seconds the presigned URL is valid for.
    Returns:
        (string): presigned URL
    """
    #url_base = "http://"+bucket_name+".s3-website-"+REGION+".amazonaws.com/"
    presigned_url = s3Client.generate_presigned_url(
        ClientMethod="get_object",
        Params={
            "Bucket": bucket_name,
            "Key": key
        },
        ExpiresIn=expires_in
    )
    return presigned_url

def img_to_url(img_file, name):
    '''
        Works with '.api/get_all_pod_symbol.py' to send img_url \n
        Args:
            img_file: Image file (e.g. from add pod card)
            name: Name of the file
        Returns:
            (string): img_url
    '''
    expires_in = 100
    objName = ((str(datetime.datetime.now()).replace(' ', '_'))+(name))
    objName = objName+".png"
    # image = Image.open(objName)
    s3ObjName = f"{FOLDER}/{objName}"
    # s3Client.Bucket(BUCKET_NAME).upload_file(img_file,s3ObjName)
    # url = self.create_presigned_urls(s3Client, BUCKET_NAME, ACCESS_KEY_ID, expires_in)
    #
    s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )
    s3.Bucket(BUCKET_NAME).put_object(Key=s3ObjName,Body=img_file,ACL='public-read')
    # s3.upload_file(
    # img_file, BUCKET_NAME, s3ObjName,
    # ExtraArgs={'ACL': 'public-read'}
    # )
    print('Uploaded img to s3')
    # public_url = f"https://{BUCKET_NAME}.s3.{REGION}.amazonaws.com/{FOLDER}...N{s3ObjName}"
    public_url = f"https://{BUCKET_NAME}.s3.{REGION}.amazonaws.com/{s3ObjName}"

    return public_url