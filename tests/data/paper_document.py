"""Dummy data for paper document.

This module contains the dummy data for paper document.

"""

import os

from app.core.config import settings
from tests.data.base import BaseDummyDataFactory


class DummyPaperDocumentFactory(BaseDummyDataFactory):
    """Dummy data factory for paper document.

    This class is responsible for the dummy data factory for paper document.

    """

    @property
    def local_storage_file_path(self):
        """Get the local storage file path.

        This method is responsible for getting the local storage file path.

        Returns:
            str: The local storage file path.

        """

        return os.path.join("tests", f"{self.paper_metadata_id}.pdf")

    @property
    def gcs_file_path(self) -> str:
        """Get the google cloud storage file path.

        This method is responsible for getting the google cloud storage file path.

        Returns:
            str: The google cloud storage file path.

        """

        return os.path.join(settings.DATA_DIR, "paper_documents", f"{self.paper_metadata_id}.pdf")
