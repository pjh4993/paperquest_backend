# -*- coding: utf-8 -*-
"""Mongo db handler module.

This module contains the mongo db handler class.

"""

import asyncio
from typing import ClassVar, Generic, Type

from beanie import PydanticObjectId, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.common.pydantic_model import PaginatedResult
from app.common.types import DOCUMENT_TYPE
from app.core.config import settings
from app.models import DOCUMENT_REGISTRY


class MongoDBSessionManager:
    """Mongo db session manager class.

    This class is responsible for handling the mongo db session.

    """

    def __init__(self):
        """Initialize the mongo db session manager.

        This method is responsible for initializing the mongo db session manager.

        """
        self.mongodb_uri = settings.MONGODB_URI
        self.mongodb_user_name = settings.MONGODB_USER_NAME
        self.mongodb_password = settings.MONGODB_USER_PASSWORD
        self.mongodb_db_name = settings.MONGODB_DB_NAME

    async def get_client(self):
        """Get the mongo db client.

        This method is responsible for getting the mongo db client.

        Returns:
            AsyncIOMotorClient: The mongo db client.

        """

        client = AsyncIOMotorClient(
            f"mongodb+srv://{self.mongodb_user_name}:{self.mongodb_password}@{self.mongodb_uri}"
        )

        try:
            ping_result = await client.admin.command("ping")
            print(self.mongodb_db_name, self.mongodb_user_name, self.mongodb_uri, ping_result)
            return client
        except Exception as e:
            print(e)
            raise e

    async def connect_to_mongodb(self):
        """Initialize the database.

        This method is responsible for initializing the database.

        """

        client = await self.get_client()
        document_models = [value for _, value in DOCUMENT_REGISTRY]
        print(document_models)
        await init_beanie(
            database=client[self.mongodb_db_name],
            document_models=document_models,  # type: ignore
        )

    async def close_connection(self):
        """Close the database connection.

        This method is responsible for closing the database connection.

        """

        client = await self.get_client()
        client.close()


class MongoDBDocumentHandler(Generic[DOCUMENT_TYPE]):
    """Mongo db document handler class

    This class is responsible for handling the mongo db.

    """

    semaphore: ClassVar[asyncio.Semaphore] = asyncio.Semaphore(settings.CONCURRENCY_LIMIT)

    def __init__(self, model: Type[DOCUMENT_TYPE]):
        """Initialize the mongo db document handler.

        This method is responsible for initializing the mongo db document handler.

        Args:
            model (DOCUMENT_TYPE): The document model.

        """

        self.model = model

    async def get(self, obj_id: PydanticObjectId) -> DOCUMENT_TYPE | None:
        """Get the document.

        This method is responsible for getting the document by bson object id.

        Args:
            obj_id (PydanticObjectId): The bson object id.

        Returns:
            DOCUMENT_TYPE: The document.

        """

        return await self.model.get(document_id=obj_id)

    async def create(self, document: DOCUMENT_TYPE) -> DOCUMENT_TYPE:
        """Create the document.

        This method is responsible for creating the document.

        Args:
            document (DOCUMENT_TYPE): The document.

        Returns:
            DOCUMENT_TYPE: The created document.

        """

        return await document.create()

    async def update_one(self, document: DOCUMENT_TYPE) -> DOCUMENT_TYPE:
        """Update the document.

        This method is responsible for updating the document.

        Args:
            document (DOCUMENT_TYPE): The document which needs to be updated.

        Returns:
            DOCUMENT_TYPE: The updated document.

        """

        return await self.model.replace(document)

    async def find_many(
        self, query: dict, limit: int, sort_query: list[tuple] | None
    ) -> PaginatedResult[DOCUMENT_TYPE]:
        """Find the documents.

        This method is responsible for finding the documents.

        Args:
            query (dict): The query.
            limit (int): The limit.
            sort_query (dict): The sort query.

        Returns:
            PaginatedResult[DOCUMENT_TYPE]: The paginated result.

        """

        cursor = self.model.find_many(query, sort=sort_query).limit(limit)

        async with MongoDBDocumentHandler.semaphore:
            total, items = await asyncio.gather(cursor.count(), cursor.to_list(length=limit))

        return PaginatedResult(total=total, items=items)
