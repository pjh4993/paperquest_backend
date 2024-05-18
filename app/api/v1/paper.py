# -*- coding: utf-8 -*-
"""Paper API Router.

This paper API router module contains the API router for the paper model.

"""

from fastapi import APIRouter, Depends

from app.common.response import CustomResponseCode, ResponseBase, ResponseModel
from app.schemas.paper_metadata import GetPaperListDetailSchema, GetPaperMetadataListParam
from app.services.paper_service import PaperService

router = APIRouter()


@router.get("/metadata")
async def get_paper_metadata_list(
    obj: GetPaperMetadataListParam = Depends(),
    paper_service: PaperService = Depends(),
) -> ResponseModel[GetPaperListDetailSchema]:
    """Get paper metadata list.

    This function is responsible for getting the paper metadata list.

    Args:
        obj (GetPaperMetadataListParam): The get paper metadata list parameter.
        paper_service (PaperService): The paper service.

    Returns:
        dict: The paper metadata list.

    """

    paper_metadata_list = await paper_service.get_paper_metadata_list(obj)

    if not paper_metadata_list:
        return await ResponseBase.failed(res=CustomResponseCode.HTTP_404)

    return await ResponseBase.success(data=paper_metadata_list)
