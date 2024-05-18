# -*- coding: utf-8 -*-
"""Paper metadata document model.

This module contains the paper metadata document model.

"""

from datetime import datetime

from beanie import Document
from pydantic import AnyHttpUrl, Field

from app.common.enums import BackgroundTaskStatus
from app.common.pydantic_model import ModelBase
from app.common.types import GCSBlobUrl
from app.models.base import DOCUMENT_REGISTRY


@DOCUMENT_REGISTRY.register
class PaperMetadata(Document, ModelBase):
    """Paper metadata document model.

    This class is responsible for the paper metadata document model.

    """

    title: str = Field(..., description="The title of the paper.")
    authors: list[str] = Field(..., description="The authors of the paper.")
    abstract: str = Field(..., description="The abstract of the paper.")
    published_at: datetime = Field(..., description="The published date of the paper.")
    venue: str = Field(..., description="The venue of the paper.")
    keywords: list[str] = Field(..., description="The keywords of the paper.")
    url: AnyHttpUrl = Field(..., description="The pdf file url of the paper.")
    gcs_blob_url: GCSBlobUrl | BackgroundTaskStatus = Field(
        default=BackgroundTaskStatus.IN_PROGRESS,
        description="""The gcs blob url of the paper if paper is uploaded to gcs.
        If background task is in progress then it will be BackgroundTaskStatus.IN_PROGRESS.
        """,
    )

    class Settings:
        """Settings for the document model."""

        collection = "paper_metadata"
        indexes = ["title", "authors", "published_at", "venue", "keywords"]
