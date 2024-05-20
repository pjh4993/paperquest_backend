# -*- coding: utf-8 -*-
"""Paper metadata repository.

This module is for paper metadata repository which manage paper metadata

"""

from beanie import PydanticObjectId
from beanie.odm.enums import SortDirection

from app.common.enums import BackgroundTaskStatus
from app.common.pydantic_model import PaginatedResult
from app.common.types import GCSBlobUrl
from app.external.database.mongo import MongoDBDocumentHandler
from app.models.paper_metadata import PaperMetadata
from app.schemas.paper_metadata import GetPaperMetadataListParam, RegisterPaperSchema


class PaperMetadataRepository(MongoDBDocumentHandler[PaperMetadata]):
    """Paper metadata repository.

    This class is responsible for paper metadata repository.

    """

    def __init__(self):
        """Initialize the paper metadata repository.

        This method is responsible for initializing the paper metadata repository.

        """

        super().__init__(model=PaperMetadata)

    async def get_metadata_by_id(self, obj_id: str) -> PaperMetadata | None:
        """Get the paper metadata by object id.

        This method is responsible for getting the paper metadata by object id.

        Args:
            obj_id (str): The object id.

        Returns:
            PaperMetadata: The paper metadata.

        """

        return await self.get(obj_id=PydanticObjectId(obj_id))

    async def register_metadata(self, obj: RegisterPaperSchema) -> PaperMetadata:
        """Register the paper metadata.

        This method is responsible for adding the paper metadata.

        Args:
            obj (PaperMetadata): The paper metadata.

        Returns:
            PaperMetadata: The added paper metadata.

        """

        return await self.create(document=PaperMetadata.model_validate(obj))

    async def update_gcs_blob_url(
        self, obj: PaperMetadata, upload_status: GCSBlobUrl | BackgroundTaskStatus
    ) -> PaperMetadata:
        """Update gcs blob url of the paper metadata.

        This method is responsible for updating the paper metadata.

        Args:
            obj (PaperMetadata): The paper metadata.
            upload_status (GCSBlobUrl | BackgroundTaskStatus): The upload status.

        Returns:
            PaperMetadata: The updated paper metadata.

        """

        obj.gcs_blob_url = upload_status

        return await self.replace(document=obj)

    async def get_metadata_list_by_page(
        self, obj: GetPaperMetadataListParam
    ) -> PaginatedResult[PaperMetadata]:
        """Get the paper metadata list by page.

        This method is responsible for getting the paper metadata list by page.

        Args:
            obj (GetPaperMetadataListParam): The get paper metadata list parameter.

        Returns:
            PaginatedResult[PaperMetadata]: The paper metadata list.

        """

        query = {}
        sort_query = None
        if obj.page_token is not None:
            query["_id"] = {"$gt": obj.page_token}
            sort_query = [("_id", SortDirection.ASCENDING)]

        return await self.find_many(
            query=query,
            limit=obj.page_size,
            sort_query=sort_query,
        )
