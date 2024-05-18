# -*- coding: utf-8 -*-
"""Base schemas for all schemas in the app."""

from typing import Generic, Optional

from beanie import PydanticObjectId
from pydantic import Field

from app.common.pydantic_model import ModelBase
from app.common.types import T


class PaginationParamSchemaBase(ModelBase):
    """Pagination parameter schema base class.

    This class is the base class for the pagination parameter schema.

    """

    page_token: Optional[PydanticObjectId] = Field(default=None, description="The page token.")
    page_size: int = Field(default=10, description="The page size.")


class PaginatedResultSchemaBase(ModelBase, Generic[T]):
    """Pagination response schema base class.

    This class is the base class for the pagination response schema.

    """

    page_token: Optional[PydanticObjectId] = Field(default=None, description="The page token.")
    page_size: int = Field(default=10, description="The page size.")
    total_items: int = Field(default=0, description="The total items for requested query")
    total_pages: int = Field(default=0, description="The total pages for requested query")
    items: list[T] = Field(default=[], description="The items for requested query")
