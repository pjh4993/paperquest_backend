"""Paper metadata repository.

This module is for paper metadata repository which manage paper metadata

"""

from beanie import PydanticObjectId

from app.common.enums import BackgroundTaskStatus
from app.common.types import GCSBlobUrl
from app.external.database.mongo import MongoDBDocumentHandler
from app.models.paper_metadata import PaperMetadata


class PaperMetadataRepository(MongoDBDocumentHandler[PaperMetadata]):
    """Paper metadata repository.

    This class is responsible for paper metadata repository.

    """

    def __init__(self):
        """Initialize the paper metadata repository.

        This method is responsible for initializing the paper metadata repository.

        """

        super().__init__(model=PaperMetadata)

    async def get_by_obj_id(self, obj_id: str) -> PaperMetadata | None:
        """Get the paper metadata by object id.

        This method is responsible for getting the paper metadata by object id.

        Args:
            obj_id (str): The object id.

        Returns:
            PaperMetadata: The paper metadata.

        """

        return await self.get(obj_id=PydanticObjectId(obj_id))

    async def register_metadata(self, obj: PaperMetadata) -> PaperMetadata:
        """Register the paper metadata.

        This method is responsible for adding the paper metadata.

        Args:
            obj (PaperMetadata): The paper metadata.

        Returns:
            PaperMetadata: The added paper metadata.

        """

        return await self.create(document=obj)

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

        return await self.update_one(document=obj)
