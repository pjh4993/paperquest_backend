# -*- coding: utf-8 -*-
"""Paper document repository.

This module is for paper pdf repository which manage paper pdf

"""

import os

from pydantic import AnyHttpUrl

from app.common.async_requests import AsyncRequestHandler
from app.common.misc import get_gcs_url
from app.common.types import GCSBlobUrl
from app.core.config import settings
from app.external.storage.google_cloud_storage import GoogleCloudStorageHandler


class PaperDocumentRepository(GoogleCloudStorageHandler, AsyncRequestHandler):
    """Paper document repository.

    This class is used to manage paper pdf.

    """

    def __init__(self):
        GoogleCloudStorageHandler.__init__(self, project_id=str(settings.GOOGLE_CLOUD_PROJECT_ID))
        AsyncRequestHandler.__init__(self)

        self.bucket_id = str(settings.GOOGLE_CLOUD_STORAGE_BUCKET_ID)

    @staticmethod
    def get_gcs_paper_blob_name(paper_obj_id: str):
        """Get google cloud storage paper document path.

        This method is used to get google cloud storage paper document path.

        Args:
            paper_obj_id (str): The paper object id.

        Returns:
            str: The google cloud storage paper document path.

        """

        return os.path.join(settings.DATA_DIR, "paper_documents", f"{paper_obj_id}.pdf")

    async def download_paper_document(self, paper_obj_id: str) -> bytes:
        """Get paper document from google cloud storage.

        This method is used to get paper document from google cloud storage.

        Args:
            paper_obj_id (str): The paper object id.

        Returns:
            bytes: The raw file bytes.

        """

        try:
            blob_name = PaperDocumentRepository.get_gcs_paper_blob_name(paper_obj_id)

            return await self.download_blob(
                bucket_name=self.bucket_id,
                source_blob_name=blob_name,
            )

        except Exception as e:
            raise e

    async def upload_paper_document(self, paper_obj_id: str, paper_url: AnyHttpUrl) -> GCSBlobUrl:
        """Upload paper document to google cloud storage.

        This method is used to upload paper document to google cloud storage.

        Args:
            paper_obj_id (str): The paper object id.
            paper_url (AnyHttpUrl): The paper url.

        Returns:
            GCSBlobUrl: The google cloud storage blob url.

        """

        try:
            response = await self.request(method="GET", url=paper_url)

            raw_paper_bytes = await response.content.read()

            blob_name = PaperDocumentRepository.get_gcs_paper_blob_name(paper_obj_id)

            await self.upload_blob(
                bucket_name=self.bucket_id,
                raw_file_bytes=raw_paper_bytes,
                destination_blob_name=blob_name,
            )

            return get_gcs_url(self.bucket_id, blob_name)

        except Exception as e:
            raise e
