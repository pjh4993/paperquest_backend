# -*- coding: utf-8 -*-
"""Common Pydantic models for the application.

This module contains the common Pydantic models for the application.

"""

import base64
from datetime import datetime
from typing import Generic

from pydantic import BaseModel, ConfigDict

from app.common.types import MODEL_TYPE
from app.core.config import settings


class ModelBase(BaseModel):
    """Model base class.

    This class is the base class for the Pydantic models.

    """

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        use_enum_values=True,
        json_encoders={
            datetime: lambda v: v.strftime(settings.DATETIME_FORMAT),
            bytes: lambda v: base64.b64encode(v).decode(),
        },
    )


class PaginatedResult(ModelBase, Generic[MODEL_TYPE]):
    """Paginated result base class.

    This class is the base class for the paginated result.

    Attributes:
        total (int): The total number of items which match the query without the pagination.
        items (list[MODEL_TYPE]): The list of items.

    """

    total: int
    items: list[MODEL_TYPE]
