"""Common Pydantic models for the application.

This module contains the common Pydantic models for the application.

"""

import base64
from datetime import datetime

from pydantic import BaseModel, ConfigDict

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
