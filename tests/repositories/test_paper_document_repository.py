# -*- coding: utf-8 -*-
"""Test for Paper document repository."""

import unittest
from unittest.mock import patch

from app.external.storage.google_cloud_storage import GoogleCloudStorageHandler
from app.repositories.paper_document import PaperDocumentRepository
from tests.data.paper import DummyPaperFactory
from tests.misc import patch_method


class TestPaperDocumentRepository(unittest.IsolatedAsyncioTestCase):
    """Test for Paper document repository."""

    def setUp(self) -> None:
        """Set up the test case."""

        self.dummy_data = DummyPaperFactory()
        with patch.object(GoogleCloudStorageHandler, "__init__", return_value=None):
            self.paper_document_repo = PaperDocumentRepository()

    @patch_method(PaperDocumentRepository.download_blob)
    async def test_download_paper_document(self, mock_download_blob):
        """Test download_paper_document method."""

        paper_metadata_id = self.dummy_data.paper_metadata_id
        raw_paper_bytes = self.dummy_data.raw_paper_bytes

        mock_download_blob.return_value = raw_paper_bytes
        result = await self.paper_document_repo.download_paper_document(
            paper_obj_id=paper_metadata_id
        )

        self.assertEqual(result, raw_paper_bytes)

    @patch_method(PaperDocumentRepository.request)
    @patch_method(PaperDocumentRepository.upload_blob)
    async def test_upload_paper_document(self, mock_upload_blob, mock_request):
        """Test upload_paper_document method."""

        paper_url = self.dummy_data.paper_url
        paper_metadata_id = self.dummy_data.paper_metadata_id
        raw_paper_bytes = self.dummy_data.raw_paper_bytes
        gcs_blob_url = self.dummy_data.gcs_blob_url

        mock_request.content.read.return_value = raw_paper_bytes

        mock_upload_blob.return_value = None
        result = await self.paper_document_repo.upload_paper_document(
            paper_obj_id=paper_metadata_id, paper_url=paper_url
        )

        self.assertEqual(result, gcs_blob_url)
