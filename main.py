import boto3
import humanize
from decouple import config


region_name = config("REGION_NAME", default="us-east-1")
aws_access_key_id = config("AWS_ACCESS_KEY_ID")
aws_secret_access_key = config("AWS_SECRET_ACCESS_KEY")
bucket_name = config("BUCKET_NAME")
file_name_prefix = config("FILE_NAME_PREFIX", "")

session = boto3.Session(
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

s3 = session.resource("s3")
my_bucket = s3.Bucket(bucket_name)

for f in my_bucket.objects.filter(Prefix=file_name_prefix):
    print(
        f.key,
        f"last_modified:{f.last_modified.strftime('%B %d, %Y at %H:%M:%S')}",
        f"size: {humanize.naturalsize(f.size)}",
    )
