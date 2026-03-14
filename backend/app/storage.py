from typing import BinaryIO

import boto3
from botocore.client import BaseClient

from app.config import Config


def get_s3_client() -> BaseClient:
    return boto3.client(
        "s3",
        endpoint_url=Config.S3_ENDPOINT or None,
        aws_access_key_id=Config.S3_ACCESS_KEY or None,
        aws_secret_access_key=Config.S3_SECRET_KEY or None,
        region_name=Config.S3_REGION,
        use_ssl=Config.S3_USE_SSL,
    )


def upload_save_file(
    file_obj: BinaryIO,
    key: str,
    content_type: str = "application/octet-stream",
) -> None:
    client = get_s3_client()
    file_obj.seek(0)
    client.upload_fileobj(
        file_obj,
        Config.S3_BUCKET,
        key,
        ExtraArgs={"ContentType": content_type},
    )
