"""Paper document repository.

This module is for paper pdf repository which manage paper pdf

"""

import os

from app.core.config import settings
from app.external.storage.google_cloud_storage import GoogleCloudStorageHandler


class PaperDocumentRepository(GoogleCloudStorageHandler):
    """Paper document repository.

    This class is used to manage paper pdf.

    """

    def __init__(self):
        super().__init__(project_id=str(settings.GOOGLE_CLOUD_PROJECT_ID))
        self.bucket_id = str(settings.GOOGLE_CLOUD_STORAGE_BUCKET_ID)
        self.data_dir_path = os.path.join(settings.DATA_DIR, "paper_documents")

    async def download_paper_document(self, paper_obj_id: str, destination_file_path: str):
        """Get paper document from google cloud storage.

        This method is used to get paper document from google cloud storage.

        Args:
            paper_obj_id (str): The paper object id.
            destination_file_path (str): The destination file path.

        Returns:
            str: The source blob name.

        """

        try:
            source_blob_name = os.path.join(self.data_dir_path, f"{paper_obj_id}.pdf")

            await self.download_blob(
                bucket_name=self.bucket_id,
                source_blob_name=source_blob_name,
                destination_file_path=destination_file_path,
            )

            return source_blob_name

        except Exception as e:
            raise e

    async def upload_paper_document(self, paper_obj_id: str, source_file_path: str):
        """Upload paper document to google cloud storage.

        This method is used to upload paper document to google cloud storage.

        Args:
            paper_obj_id (str): The paper object id.
            source_file_path (str): The source file path.

        Returns:
            str: The destination blob name.

        """

        try:
            destination_blob_name = os.path.join(self.data_dir_path, f"{paper_obj_id}.pdf")

            await self.upload_blob(
                bucket_name=self.bucket_id,
                source_file_path=source_file_path,
                destination_blob_name=destination_blob_name,
            )

            return destination_blob_name

        except Exception as e:
            raise e
