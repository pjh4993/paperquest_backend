# -*- coding: utf-8 -*-
"""Dummy data for paper document.

This module contains the dummy data for paper document.

"""

from app.common.misc import get_gcs_url
from app.common.pydantic_model import PaginatedResult
from app.common.types import GCSBlobUrl
from app.core.config import settings
from app.models.paper_metadata import PaperMetadata
from app.repositories.paper_document import PaperDocumentRepository
from app.schemas.paper_metadata import (
    GetPaperListDetailSchema,
    GetPaperMetadataListParam,
    RegisterPaperSchema,
)
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
    def paginated_paper_metadata(self) -> PaginatedResult[PaperMetadata]:
        """Get the paginated paper metadata.

        This method is responsible for getting the paginated paper metadata.

        Returns:
            PaginatedResult[PaperMetadata]: The paginated paper metadata.

        """

        return PaginatedResult[PaperMetadata](
            total=1,
            items=[self.paper_metadata_model],
        )

    @property
    def get_paper_metadata_list_param(self) -> GetPaperMetadataListParam:
        """Get the get paper metadata list parameter.

        This method is responsible for getting the get paper metadata list parameter.

        Returns:
            GetPaperMetadataListParam: The get paper metadata list parameter.

        """

        return GetPaperMetadataListParam.model_validate(
            {
                "page_token": None,
                "page_size": 1,
            }
        )

    @property
    def register_paper_schema(self) -> RegisterPaperSchema:
        """Get the register paper schema.

        This method is responsible for getting the register paper schema.

        Returns:
            RegisterPaperSchema: The register paper schema.

        """

        return RegisterPaperSchema.model_validate(self.paper_metadata_json)

    @property
    def get_paper_list_detail_schema(self) -> GetPaperListDetailSchema:
        """Get the get paper list detail schema.

        This method is responsible for getting the get paper list detail schema.

        Returns:
            GetPaperListDetailSchema: The get paper list detail schema.

        """

        return GetPaperListDetailSchema.model_validate(
            {
                "page_token": self.paper_metadata_id,
                "page_size": self.get_paper_metadata_list_param.page_size,
                "total_pages": 1,
                "total_items": 1,
                "items": [self.paper_metadata_model],
            }
        )
