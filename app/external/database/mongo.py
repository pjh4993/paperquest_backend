"""Mongo db handler module.

This module contains the mongo db handler class.

"""

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

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
            print(ping_result)
            return client
        except Exception as e:
            print(e)
            raise e

    async def initialize_database(self):
        """Initialize the database.

        This method is responsible for initializing the database.

        """

        client = await self.get_client()
        document_models = [value for _, value in DOCUMENT_REGISTRY]
        print(document_models)
        await init_beanie(
            database=client.paper_quest,
            document_models=document_models,  # type: ignore
        )
