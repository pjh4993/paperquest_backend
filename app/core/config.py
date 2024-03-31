"""Base settings for the application."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Base settings for the application.

    This class is used to define the base settings for the application.

    Attributes:
        model_config (SettingsConfigDict): The settings configuration model.
        app_name (str): The name of the application.
        app_version (str): The version of the application.
        app_description (str): The description of the application.
        app_debug (bool): The debug mode of the application.
        app_testing (bool): The testing mode of the application.
        server_host (str): The host of the server.

    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # App settings
    VERSION: str = "0.0.1"
    DESCRIPTION: str = "PaperQuest-Backend"

    # Uvicorn settings
    UVICORN_HOST: str = "localhost"
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True

    # Mongodb settings
    MONGODB_URI: str | None = None
    MONGODB_USER_NAME: str | None = None
    MONGODB_USER_PASSWORD: str | None = None
    MONGODB_DB_NAME: str = "PaperQuest"

    # Data directory settings
    DATA_DIR: str = "andrew/paperquest/data"

    # Google cloud storage settings
    GOOGLE_CLOUD_PROJECT_ID: str | None = None
    GOOGLE_CLOUD_STORAGE_BUCKET_ID: str | None = None

    # Local storage settings
    LOCAL_STORAGE_PATH: str = "/artifacts"


settings = Settings()
