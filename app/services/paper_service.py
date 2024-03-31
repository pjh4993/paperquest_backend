"""Paper service module.

This module contains the service for the paper model.

"""

from app.common.enums import BackgroundTaskStatus
from app.common.exceptions import NotFoundError
from app.models.paper_metadata import PaperMetadata
from app.repositories.paper_document import PaperDocumentRepository
from app.repositories.paper_metadata import PaperMetadataRepository
from app.schemas.paper import RegisterPaperSchema


class PaperService:
    """Paper service class.

    This class contains the service for the paper model.

    """

    def __init__(self):
        """Initialize the paper service class."""

        self.paper_metadata_repo = PaperMetadataRepository()
        self.paper_document_repo = PaperDocumentRepository()

    async def upload_paper_document(self, obj: PaperMetadata, paper_obj_id: str) -> PaperMetadata:
        """Upload paper document.

        This method uploads the paper document.

        Args:
            obj (PaperMetadata): The paper metadata.j
            paper_obj_id (str): The paper object id.

        Returns:
            PaperMetadata: The updated paper metadata.

        """

        upload_result = await self.paper_document_repo.upload_paper_document(
            paper_obj_id=paper_obj_id, paper_url=obj.url
        )

        if upload_result is None:
            upload_result = BackgroundTaskStatus.FAILED

        updated = await self.paper_metadata_repo.update_gcs_blob_url(obj, upload_result)

        return updated

    async def register_paper(self, obj: RegisterPaperSchema) -> PaperMetadata:
        """Register a paper.

        This method registers a paper.

        Args:
            obj (RegisterPaperSchema): The register paper schema.

        Returns:
            PaperMetadata: The registered paper metadata.

        """

        result = await self.paper_metadata_repo.register_metadata(PaperMetadata.model_validate(obj))

        if result is None or result.id is None:
            raise NotFoundError(f"Failed to register paper metadata with {obj}")

        return result

    async def get_paper_metadata(self, paper_obj_id: str) -> PaperMetadata | None:
        """Get paper metadata.

        This method gets the paper metadata.

        Args:
            paper_obj_id (str): The paper object id.

        Returns:
            PaperMetadata: The paper metadata.

        """

        return await self.paper_metadata_repo.get_by_obj_id(paper_obj_id)
