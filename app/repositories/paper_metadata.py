"""Paper metadata repository.

This module is for paper metadata repository which manage paper metadata

"""

from beanie import PydanticObjectId

from app.external.database.mongo import MongoDBDocumentHandler
from app.models.paper_metadata import PaperMetadata


class PaperMetadataRepository(MongoDBDocumentHandler[PaperMetadata]):
    """Paper metadata repository.

    This class is responsible for paper metadata repository.

    """

    async def get_by_obj_id(self, obj_id: str) -> PaperMetadata | None:
        """Get the paper metadata by object id.

        This method is responsible for getting the paper metadata by object id.

        Args:
            obj_id (str): The object id.

        Returns:
            PaperMetadata: The paper metadata.

        """

        return await self.get(obj_id=PydanticObjectId(obj_id))

    async def add(self, paper_metadata: PaperMetadata) -> PaperMetadata:
        """Add the paper metadata.

        This method is responsible for adding the paper metadata.

        Args:
            paper_metadata (PaperMetadata): The paper metadata.

        Returns:
            PaperMetadata: The added paper metadata.

        """

        return await self.create(document=paper_metadata)
