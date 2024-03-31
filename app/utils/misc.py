"""Mischellaneous utility functions"""

from app.common.types import GCSBlobUrl


def get_gcs_url(bucket_id: str, blob_name: str) -> GCSBlobUrl:
    """Get google cloud storage url.

    This function is used to get google cloud storage url.

    Args:
        bucket_id (str): The bucket id.
        blob_name (str): The blob name.

    Returns:
        GCSBlobUrl: The google cloud storage url.

    """

    return f"gs://{bucket_id}/{blob_name}"
