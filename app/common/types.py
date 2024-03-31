"""Type utility for the application.

This module is for type utility for the application.

"""

from typing import TypeVar

from beanie import Document

DOCUMENT_TYPE = TypeVar("DOCUMENT_TYPE", bound=Document)
