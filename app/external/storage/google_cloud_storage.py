"""Google cloud storage handler module

This module contains the google cloud storage handler class.

"""

from fastapi.concurrency import run_in_threadpool
from google.cloud.storage import Blob, Client


class GoogleCloudStorageHandler:
    """Google cloud storage handler class

    This class is responsible for handling the google cloud storage.

    """

    def __init__(self, project_id: str):
        """Initialize the google cloud storage handler

        This method is responsible for initializing the google cloud storage handler.

        Args:
            project_id (str): The project id.

        """

        self.client = Client(project=project_id)

    def get_bucket(self, bucket_name: str):
        """Get the bucket

        This method is responsible for getting the bucket.

        Args:
            bucket_name (str): The bucket name.

        Returns:
            Bucket: The bucket.

        """

        return self.client.get_bucket(bucket_name)

    async def upload_blob(
        self, bucket_name: str, raw_file_bytes: bytes, destination_blob_name: str
    ) -> Blob:
        """Upload the blob

        This method is responsible for uploading the blob.

        Args:
            bucket_name (str): The bucket name.
            raw_file_bytes (bytes): The raw file bytes.
            destination_blob_name (str): The destination blob name.

        Returns:
            Blob: The blob uploaded.

        """

        bucket = self.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        await run_in_threadpool(blob.upload_from_string, raw_file_bytes)

        return blob

    async def get_blob_metadata(self, bucket_name: str, blob_name: str) -> Blob | None:
        """Get the blob metadata

        This method is responsible for getting the blob metadata.

        Args:
            bucket_name (str): The bucket name.
            blob_name (str): The blob name.

        Returns:
            Blob: The blob.

        """

        bucket = self.get_bucket(bucket_name)
        blob = await run_in_threadpool(bucket.get_blob, blob_name)

        return blob

    async def download_blob(self, bucket_name: str, source_blob_name: str) -> bytes:
        """Download the blob

        This method is responsible for downloading the blob.

        Args:
            bucket_name (str): The bucket name.
            source_blob_name (str): The source blob name.

        Returns:
            bytes: The downloaded blob.

        """

        bucket = self.get_bucket(bucket_name)
        blob = bucket.blob(source_blob_name)

        return await run_in_threadpool(blob.download_as_bytes)
