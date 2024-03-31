"""Dummy data for paper document.

This module contains the dummy data for paper document.

"""

from app.common.types import GCSBlobUrl
from app.core.config import settings
from app.models.paper_metadata import PaperMetadata
from app.repositories.paper_document import PaperDocumentRepository
from app.schemas.paper import RegisterPaperSchema
from app.utils.misc import get_gcs_url
from tests.data.base import BaseDummyDataFactory


class DummyPaperFactory(BaseDummyDataFactory):
    """Dummy data factory for paper data.

    This class is responsible for the dummy data factory for paper.

    """

    @property
    def gcs_blob_url(self) -> GCSBlobUrl:
        """Get the google cloud storage file path.

        This method is responsible for getting the google cloud storage file path.

        Returns:
            GCSBlobUrl: The google cloud storage file path.

        """

        return get_gcs_url(
            str(settings.GOOGLE_CLOUD_STORAGE_BUCKET_ID),
            PaperDocumentRepository.get_gcs_paper_blob_name(self.paper_metadata_id),
        )

    @property
    def paper_metadata_model(self) -> PaperMetadata:
        """Get the paper metadata.

        This method is responsible for getting the paper metadata.

        Returns:
            PaperMetadata: The paper metadata.

        """

        return PaperMetadata.model_validate(self.paper_metadata_json)

    @property
    def register_paper_schema(self) -> RegisterPaperSchema:
        """Get the register paper schema.

        This method is responsible for getting the register paper schema.

        Returns:
            RegisterPaperSchema: The register paper schema.

        """

        return RegisterPaperSchema.model_validate(self.paper_metadata_json)
