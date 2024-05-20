# -*- coding: utf-8 -*-
"""Paper API Router.

This paper API router module contains the API router for the paper model.

"""

from fastapi import APIRouter, Depends

from app.common.response import CustomResponseCode, ResponseBase, ResponseModel
from app.schemas.paper_metadata import (
    GetPaperDetailSchema,
    GetPaperListDetailSchema,
    GetPaperMetadataListParam,
    RegisterPaperSchema,
)
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
        ResponseModel[GetPaperListDetailSchema]: The paper metadata list.

    """

    paper_metadata_list = await paper_service.get_paper_metadata_list(obj)

    if not paper_metadata_list:
        return await ResponseBase.failed(res=CustomResponseCode.HTTP_404)

    return await ResponseBase.success(data=paper_metadata_list)


@router.post("")
async def register_paper(
    obj: RegisterPaperSchema,
    paper_service: PaperService = Depends(),
) -> ResponseModel[GetPaperDetailSchema]:
    """Register paper.

    This function is responsible for registering a paper.

    Args:
        obj (RegisterPaperSchema): The register paper schema.
        paper_service (PaperService): The paper service.

    Returns:
        ResponseModel[GetPaperDetailSchema]: The registered paper.

    """

    result = await paper_service.register_paper(obj=obj)

    if result is None:
        return await ResponseBase.failed(res=CustomResponseCode.HTTP_404)

    return await ResponseBase.success(data=result)
