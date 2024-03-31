"""Test cases for the paper service."""

import unittest
from unittest.mock import patch

from app.models.paper_metadata import PaperMetadata
from app.repositories.paper_document import PaperDocumentRepository
from app.repositories.paper_metadata import PaperMetadataRepository
from app.services.paper_service import PaperService
from tests.data.paper import DummyPaperFactory
from tests.misc import patch_method
from tests.session.mongo import MockMongoDBSession


class TestPaperService(unittest.IsolatedAsyncioTestCase):
    """Test cases for the paper service."""

    def setUp(self) -> None:
        self.dummy_data = DummyPaperFactory()

        self.mock_mongo_session = MockMongoDBSession()

        with (
            patch.object(PaperMetadataRepository, "__init__", return_value=None),
            patch.object(PaperDocumentRepository, "__init__", return_value=None),
        ):
            self.paper_service = PaperService()

    async def asyncSetUp(self) -> None:

        await self.mock_mongo_session.connect_to_mock_mongo([PaperMetadata])

    @patch_method(PaperDocumentRepository.upload_paper_document)
    @patch_method(PaperMetadataRepository.update_gcs_blob_url)
    async def test_upload_paper_document(
        self,
        mock_update_gcs_blob_url,
        mock_upload_paper_document,
    ):

        paper_metadata = self.dummy_data.paper_metadata_model
        paper_obj_id = self.dummy_data.paper_metadata_id

        mock_upload_paper_document.return_value = self.dummy_data.gcs_blob_url
        mock_update_gcs_blob_url.return_value = paper_metadata

        result = await self.paper_service.upload_paper_document(paper_metadata, paper_obj_id)

        self.assertEqual(result, paper_metadata)

    @patch_method(PaperMetadataRepository.register_metadata)
    async def test_register_paper(self, mock_register_metadata):

        paper_metadata = self.dummy_data.paper_metadata_model

        mock_register_metadata.return_value = paper_metadata

        result = await self.paper_service.register_paper(self.dummy_data.register_paper_schema)

        self.assertEqual(result, paper_metadata)

    @patch_method(PaperMetadataRepository.get_by_obj_id)
    async def test_get_paper_metadta(self, mock_get_by_obj_id):
        paper_metadata = self.dummy_data.paper_metadata_model
        paper_obj_id = self.dummy_data.paper_metadata_id

        mock_get_by_obj_id.return_value = paper_metadata

        result = await self.paper_service.get_paper_metadata(paper_obj_id)

        self.assertEqual(result, paper_metadata)