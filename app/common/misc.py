# -*- coding: utf-8 -*-
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


def count_total_pages(total: int, page_size: int) -> int:
    """Count total pages.

    This function is used to count total pages.

    Args:
        total (int): The total.
        page_size (int): The page size.

    Returns:
        int: The total pages.

    """

    return (total + page_size - 1) // page_size
