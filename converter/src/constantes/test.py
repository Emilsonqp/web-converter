
import boto3
from enum import Enum


class S3CustomKeys(Enum):
    AWS_ACCESS_KEY_ID = 'ASIAWRNPKSN4T3K4UJ74'
    AWS_SECRET_ACCESS_KEY = 'rYRfY0eCqjfg2x4fiJqM73jnzaaFNc0AdET9Q9nR'
    AWS_SESSION_TOKEN = 'FwoGZXIvYXdzEF4aDL1kEGbzYoL1EoS3biLLAQKzVcVFqkazFOAp4ELwzhj0OTBwJyuw8E5yUCTgfdCq0q9qs/qq2qggSI5SnwJn/1dA/6nl1664/s8DuieUoAxdwBnuWqomccWv1UyMAV++FPyQPSneOH3/Puuh3tYR8yEooZtLwp9pKnN+6vJS1TCiE3CBDXDkOz/NB9SAdBsizO7goqukGXW6ETOaYtwWfT9NKPK/TkIxNfxjkkm7hnnEjNNMUMPNhH3okBfCdzSv5vNe83NOQ19L2TnQS53kPI5C6E06Zkir69PrKJn66IwGMi1JYYuJONJp/sdqM7RQuhvEgSfvU1O69HAU3K7n/nE//CzRWiSl82TdOMVuAV4='

class S3Client:
    def __init__(self):
        self.client = boto3.client('s3', aws_access_key_id     = S3CustomKeys.AWS_ACCESS_KEY_ID.value,
                                         aws_secret_access_key = S3CustomKeys.AWS_SECRET_ACCESS_KEY.value,
                                         aws_session_token     = S3CustomKeys.AWS_SESSION_TOKEN.value)
recordings_bucket = 'recordingsbucket01'



client = S3Client().client
path = "./constantes.py"
client.upload_file(path,recordings_bucket,path)