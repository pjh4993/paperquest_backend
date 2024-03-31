"""Dummy data factory for paper metadata.

This module contains the dummy data factory for paper metadata.

"""

from app.models.paper_metadata import PaperMetadata
from tests.data.base import BaseDummyDataFactory


class DummyPaperMetadataFactory(BaseDummyDataFactory):
    """Dummy data factory for paper metadata.

    This class is responsible for the dummy data factory for paper metadata.

    """

    def __init__(self):
        super().__init__()

        self.paper_metadata_id = BaseDummyDataFactory.generate_random_obj_id()

    @property
    def paper_metadata_model(self) -> PaperMetadata:
        """Get the paper metadata.

        This method is responsible for getting the paper metadata.

        Returns:
            PaperMetadata: The paper metadata.

        """

        return PaperMetadata.model_validate(self.paper_metadata_json)
