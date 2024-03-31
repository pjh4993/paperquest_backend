"""Register stage of Fast api application.

This module contains the register stage of the Fast api application.

"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.datastructures import State

from app.core.config import settings
from app.external.database.mongo import MongoDBSessionManager


class AppState(State):
    """Application state class.

    This class is responsible for the application state.

    """

    mongodb_session_manager: MongoDBSessionManager

    def __init__(self):
        """Initialize the application state.

        This method is responsible for initializing the application state.

        """

        super().__init__()
        self.mongodb_session_manager = MongoDBSessionManager()


@asynccontextmanager
async def lifecycle(app: FastAPI):
    """ "Lifecycle context manager.

    This context manager is responsible for the lifecycle of the application.

    Args:
        app (FastAPI): The FastAPI application.

    """

    if not isinstance(app.state, AppState):
        app.state = AppState()

    await app.state.mongodb_session_manager.initialize_database()

    yield


def init_app():
    """Initialize the application."""

    app = FastAPI(
        title="PaperQuest-Backend",
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        state=AppState(),
        lifespan=lifecycle,
    )

    return app
