# -*- coding: utf-8 -*-
"""Test cases for the paper API endpoints."""

import unittest
from unittest.mock import patch

from fastapi import FastAPI
from httpx import AsyncClient

from app.api.v1.paper import router as paper_router
from app.models.paper_metadata import PaperMetadata
from app.services.paper_service import PaperService
from tests.data.paper import DummyPaperFactory
from tests.misc import patch_method
from tests.session.mongo import MockMongoDBSession


class TestPaperRoute(unittest.IsolatedAsyncioTestCase):
    """Test Paper route"""

    def setUp(self):
        """Set up test."""

        self.host = "http://test"
        self.base_path = "/api/v1/paper"
        self.mock_mongo_session = MockMongoDBSession()

        with patch.object(PaperService, "__init__", return_value=None):
            self.mock_service = PaperService()

        self.mock_app = FastAPI()
        self.mock_app.include_router(paper_router, prefix=self.base_path)
        self.mock_app.dependency_overrides[PaperService] = self.get_mock_paper_service
        self.dummy_data = DummyPaperFactory()

    async def asyncSetUp(self):
        """Set up async test."""

        self.async_client = AsyncClient(app=self.mock_app, base_url=self.host)
        await self.mock_mongo_session.connect_to_mock_mongo([PaperMetadata])

    async def get_mock_paper_service(self) -> PaperService:
        """Mock get paper service"""

        return self.mock_service

    @patch_method(PaperService.get_paper_metadata_list)
    async def test_async_get_paper_metadata_list(self, mock_get_paper_metadata_list) -> None:
        """Test get paper metadata list"""

        mock_get_paper_metadata_list.return_value = self.dummy_data.get_paper_list_detail_schema
        params = self.dummy_data.get_paper_metadata_list_param.model_dump(mode="json")
        expected_result = self.dummy_data.get_paper_list_detail_schema

        response = await self.async_client.get(f"{self.base_path}/metadata", params=params)
        response_data = response.json()

        self.assertEqual(response_data["code"], 200)
        self.assertEqual(response_data["data"], expected_result)
