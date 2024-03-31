"""Paper schema module.

This module contains the paper schema.

"""

from datetime import datetime

from pydantic import AnyHttpUrl, Field

from app.common.pydantic_model import ModelBase


class PaperSchemaBase(ModelBase):
    """Paper schema base class.

    This class is the base class for the paper schema.

    """

    title: str = Field(..., description="The title of the paper.")
    authors: list[str] = Field(..., description="The authors of the paper.")
    abstract: str = Field(..., description="The abstract of the paper.")
    published_at: datetime = Field(..., description="The published date of the paper.")
    venue: str = Field(..., description="The venue of the paper.")
    keywords: list[str] = Field(..., description="The keywords of the paper.")
    url: AnyHttpUrl = Field(..., description="The pdf file url of the paper.")


class RegisterPaperSchema(PaperSchemaBase):
    """Register paper schema.

    This class is responsible for the register paper schema.

    """


class GetPaperDetailSchema(PaperSchemaBase):
    """Get paper detail schema.

    This class is responsible for the get paper detail schema.

    """
