import os
import boto3
import uuid

from app.core.config import settings


s3_client = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION
)


def upload_file_to_s3(file):
    extension = file.filename.split(".")[-1]

    object_name = f"{uuid.uuid4()}.{extension}"

    s3_client.upload_fileobj(
        file.file,
        settings.AWS_BUCKET_NAME,
        object_name
    )

    return object_name


def download_file_from_s3(object_name):
    temp_path = os.path.join(
        "temp",
        object_name
    )

    os.makedirs("temp", exist_ok=True)

    s3_client.download_file(
        settings.AWS_BUCKET_NAME,
        object_name,
        temp_path
    )

    return temp_path


def delete_file_from_s3(object_name):
    s3_client.delete_object(
        Bucket=settings.AWS_BUCKET_NAME,
        Key=object_name
    )