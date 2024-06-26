# -*- coding: utf-8 -*-
"""Test cases for the paper metadata repository."""

import unittest
from unittest.mock import patch

from app.external.database.mongo import MongoDBDocumentHandler
from app.models.paper_metadata import PaperMetadata
from app.repositories.paper_metadata import PaperMetadataRepository
from tests.data.paper import DummyPaperFactory
from tests.misc import patch_method
from tests.session.mongo import MockMongoDBSession


class TestPaperMetadataRepository(unittest.IsolatedAsyncioTestCase):
    """Test cases for the paper metadata repository."""

    def setUp(self) -> None:
        """Set up the test case."""

        self.mock_session = MockMongoDBSession()
        self.dummy_data = DummyPaperFactory()

        with patch.object(MongoDBDocumentHandler, "__init__", return_value=None):
            self.repo = PaperMetadataRepository()

    async def asyncSetUp(self) -> None:
        """Set up the async test case."""

        await self.mock_session.connect_to_mock_mongo(models=[PaperMetadata])

    @patch_method(PaperMetadataRepository.get)
    async def test_get_by_obj_id(self, mock_get):
        """Test get_by_obj_id method."""

        obj_id = self.dummy_data.paper_metadata_id
        paper_metadata_model = self.dummy_data.paper_metadata_model
        mock_get.return_value = paper_metadata_model

        result = await self.repo.get_metadata_by_id(obj_id=obj_id)

        self.assertEqual(result, paper_metadata_model)

    @patch_method(PaperMetadataRepository.create)
    async def test_register_metadata(self, mock_create):
        """Test add method."""

        obj = self.dummy_data.register_paper_schema
        paper_metadata_model = self.dummy_data.paper_metadata_model
        mock_create.return_value = paper_metadata_model

        result = await self.repo.register_metadata(obj=obj)

        self.assertEqual(result, paper_metadata_model)

    @patch_method(PaperMetadataRepository.replace)
    async def test_update_gcs_blob_url(self, mock_update_one):
        """Test update_gcs_blob_url method."""

        paper_metadata_model = self.dummy_data.paper_metadata_model
        gcs_blob_url = self.dummy_data.gcs_blob_url
        mock_update_one.return_value = paper_metadata_model

        result = await self.repo.update_gcs_blob_url(
            obj=paper_metadata_model, upload_status=gcs_blob_url
        )

        self.assertEqual(result, paper_metadata_model)

    @patch_method(PaperMetadataRepository.find_many)
    async def test_get_metadata_list(self, mock_find):
        """Test get_metadata_list method."""

        obj = self.dummy_data.get_paper_metadata_list_param
        paginated_paper_metadata = self.dummy_data.paginated_paper_metadata
        mock_find.return_value = paginated_paper_metadata

        result = await self.repo.get_metadata_list_by_page(obj=obj)

        self.assertEqual(result, paginated_paper_metadata)
