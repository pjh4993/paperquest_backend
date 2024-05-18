# -*- coding: utf-8 -*-
"""Response schema

This module contains response schema

"""

from typing import Any, Generic, Optional

from app.common.pydantic_model import ModelBase
from app.common.response.response_code import CustomResponseCode
from app.common.types import MODEL_TYPE


class ResponseModel(ModelBase, Generic[MODEL_TYPE]):
    """Response model

    This class is used to define response model

    """

    code: int = CustomResponseCode.HTTP_200.code
    msg: str = CustomResponseCode.HTTP_200.msg
    data: Optional[MODEL_TYPE] = None


class ResponseBase:
    """Response base

    This class is used to define response base

    """

    @staticmethod
    async def _response(
        res: CustomResponseCode | None = None, data: Optional[Any] = None
    ) -> ResponseModel[Any]:
        """Response

        Args:
            res (CustomResponseCode): custom response code
            data (Any): response data

        Returns:
            ResponseModel: response model

        """

        if res is None:
            res = CustomResponseCode.UNKNOWN
        return ResponseModel(code=res.code, msg=res.msg, data=data)

    @staticmethod
    async def success(
        res: CustomResponseCode = CustomResponseCode.HTTP_200,
        data: Optional[Any] = None,
    ) -> ResponseModel[Any]:
        """Success

        Args:
            res (CustomResponseCode): custom response code
            data (Any): response data

        Returns:
            ResponseModel: response model

        """

        return await ResponseBase._response(res=res, data=data)

    @staticmethod
    async def failed(
        res: CustomResponseCode = CustomResponseCode.HTTP_400,
        data: Optional[Any] = None,
    ) -> ResponseModel[Any]:
        """Failed

        Args:
            res (CustomResponseCode): custom response code
            data (Any): response data

        Returns:
            ResponseModel: response model

        """

        return await ResponseBase._response(res=res, data=data)
