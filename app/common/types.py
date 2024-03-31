"""Type utility for the application.

This module is for type utility for the application.

"""

from typing import Annotated, TypeVar

from beanie import Document
from pydantic import StringConstraints

DOCUMENT_TYPE = TypeVar("DOCUMENT_TYPE", bound=Document)

GCSBlobUrl = Annotated[str, StringConstraints(pattern=r"gs://.*")]
