"""Main file for the project. This file will be used to run the project.

This file will be used to run the project.

"""

from pathlib import Path

import uvicorn

from app.core.config import settings
from app.core.register import init_app

app = init_app()

if __name__ == "__main__":
    uvicorn.run(
        app=Path(__file__).stem + ":app",
        host=settings.UVICORN_HOST,
        port=settings.UVICORN_PORT,
        reload=settings.UVICORN_RELOAD,
    )
