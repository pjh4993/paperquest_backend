"""Test for Paper document repository."""

import unittest
from unittest.mock import patch

from app.external.storage.google_cloud_storage import GoogleCloudStorageHandler
from app.repositories.paper_document import PaperDocumentRepository
from tests.data.paper_document import DummyPaperDocumentFactory
from tests.misc import patch_method


class TestPaperDocumentRepository(unittest.IsolatedAsyncioTestCase):
    """Test for Paper document repository."""

    def setUp(self) -> None:
        self.dummy_data = DummyPaperDocumentFactory()
        with patch.object(GoogleCloudStorageHandler, "__init__", return_value=None):
            self.paper_document_repo = PaperDocumentRepository()

    @patch_method(PaperDocumentRepository.download_blob)
    async def test_download_paper_document(self, mock_download_blob):

        paper_metadata_id = self.dummy_data.paper_metadata_id
        destination_file_path = self.dummy_data.local_storage_file_path
        source_blob_name = self.dummy_data.gcs_file_path

        mock_download_blob.return_value = None
        result = await self.paper_document_repo.download_paper_document(
            paper_obj_id=paper_metadata_id, destination_file_path=destination_file_path
        )

        self.assertEqual(result, source_blob_name)

    @patch_method(PaperDocumentRepository.upload_blob)
    async def test_upload_paper_document(self, mock_upload_blob):

        paper_metadata_id = self.dummy_data.paper_metadata_id
        source_file_path = self.dummy_data.local_storage_file_path
        dest_blob_name = self.dummy_data.gcs_file_path

        mock_upload_blob.return_value = None
        result = await self.paper_document_repo.upload_paper_document(
            paper_obj_id=paper_metadata_id, source_file_path=source_file_path
        )

        self.assertEqual(result, dest_blob_name)
