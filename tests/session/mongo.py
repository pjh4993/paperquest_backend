# -*- coding: utf-8 -*-
"""Mock MongoDB session

This module contains mock MongoDB session.

"""

from typing import cast

from beanie import init_beanie
from mongomock_motor import AsyncMongoMockClient
from motor.core import AgnosticDatabase


class MockMongoDBSession:
    """Mock MongoDB session

    This class is used to define mock MongoDB session.

    Attributes:
        client (AsyncMongoMockClient): Mock MongoDB client

    """

    def __init__(self) -> None:
        """Initialize mock MongoDB session"""

        self.client: AsyncMongoMockClient = AsyncMongoMockClient()

    async def connect_to_mock_mongo(self, models: list) -> None:
        """Connect to mock mongo

        Args:
            models (list): List of models

        """

        db = cast(AgnosticDatabase, self.client.test_pyler)
        await init_beanie(
            database=db,  # type: ignore
            document_models=models,
        )
