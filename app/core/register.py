# -*- coding: utf-8 -*-
"""Register stage of Fast api application.

This module contains the register stage of the Fast api application.

"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.datastructures import State

from app.api.routers import v1_router
from app.core.config import settings
from app.external.database.mongo import MongoDBSessionManager


class SessionStatae(State):
    """Application state class for managing session.

    This class is responsible for the application state.

    """

    mongodb_session_manager: MongoDBSessionManager

    def __init__(self):
        """Initialize the application state.

        This method is responsible for initializing the application state.

        """

        super().__init__()
        self.mongodb_session_manager = MongoDBSessionManager()

    async def connect(self):
        """Connect to the database.

        This method is responsible for connecting to the database.

        """

        await self.mongodb_session_manager.connect_to_mongodb()

    async def close(self):
        """Close the database connection.

        This method is responsible for closing the database connection.

        """

        await self.mongodb_session_manager.close_connection()


@asynccontextmanager
async def lifecycle(app: FastAPI):
    """Lifecycle context manager.

    This context manager is responsible for the lifecycle of the application.

    Args:
        app (FastAPI): The FastAPI application.

    """

    session_state = SessionStatae()

    await session_state.connect()

    yield

    await session_state.close()


def register_router(app: FastAPI) -> None:
    """Register routers

    Args:
        app (FastAPI): FastAPI application

    """

    app.include_router(v1_router)


def register_middleware(app: FastAPI) -> None:
    """Register middlewares"""

    pass


def init_app():
    """Initialize the application."""

    app = FastAPI(
        title="PaperQuest-Backend",
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        state=SessionStatae(),
        lifespan=lifecycle,
    )

    register_router(app)

    register_middleware(app)

    return app
