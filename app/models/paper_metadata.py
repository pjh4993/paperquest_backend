"""Paper metadata document model.

This module contains the paper metadata document model.

"""

from datetime import datetime

from beanie import Document
from pydantic import Field

from app.models.base import DOCUMENT_REGISTRY


@DOCUMENT_REGISTRY.register
class PaperMetadata(Document):
    """Paper metadata document model.

    This class is responsible for the paper metadata document model.

    """

    title: str = Field(..., description="The title of the paper.")
    authors: list[str] = Field(..., description="The authors of the paper.")
    abstract: str = Field(..., description="The abstract of the paper.")
    published_at: datetime = Field(..., description="The published date of the paper.")
    venue: str = Field(..., description="The venue of the paper.")
    keywords: list[str] = Field(..., description="The keywords of the paper.")
