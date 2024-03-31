"""Test cases for the paper metadata repository."""

import unittest
from unittest.mock import patch

from app.external.database.mongo import MongoDBDocumentHandler
from app.models.paper_metadata import PaperMetadata
from app.repositories.paper_metadata import PaperMetadataRepository
from tests.data.paper_metadata import DummyPaperMetadataFactory
from tests.misc import patch_method
from tests.session.mongo import MockMongoDBSession


class TestPaperMetadataRepository(unittest.IsolatedAsyncioTestCase):
    """Test cases for the paper metadata repository."""

    def setUp(self) -> None:
        self.mock_session = MockMongoDBSession()
        self.dummy_data = DummyPaperMetadataFactory()

        with patch.object(MongoDBDocumentHandler, "__init__", return_value=None):
            self.repo = PaperMetadataRepository()

    async def asyncSetUp(self) -> None:
        await self.mock_session.connect_to_mock_mongo(models=[PaperMetadata])

    @patch_method(PaperMetadataRepository.get)
    async def test_get_by_obj_id(self, mock_get):
        """Test get_by_obj_id method."""

        obj_id = self.dummy_data.paper_metadata_id
        paper_metadata_model = self.dummy_data.paper_metadata_model
        mock_get.return_value = paper_metadata_model

        result = await self.repo.get_by_obj_id(obj_id=obj_id)

        self.assertEqual(result, paper_metadata_model)

    @patch_method(PaperMetadataRepository.create)
    async def test_add(self, mock_create):
        """Test add method."""

        paper_metadata_model = self.dummy_data.paper_metadata_model
        mock_create.return_value = paper_metadata_model

        result = await self.repo.add(paper_metadata=paper_metadata_model)

        self.assertEqual(result, paper_metadata_model)
