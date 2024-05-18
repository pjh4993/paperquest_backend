# -*- coding: utf-8 -*-
"""Type utility for the application.

This module is for type utility for the application.

"""

from typing import Annotated, TypeVar

from beanie import Document
from pydantic import BaseModel, StringConstraints

DOCUMENT_TYPE = TypeVar("DOCUMENT_TYPE", bound=Document)
MODEL_TYPE = TypeVar("MODEL_TYPE", bound=BaseModel)

T = TypeVar("T")

GCSBlobUrl = Annotated[str, StringConstraints(pattern=r"gs://.*")]
