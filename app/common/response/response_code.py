# -*- coding: utf-8 -*-
"""Custom response code

This module contains custom response code

"""

from enum import Enum


class CustomCodeBase(Enum):
    """Custom code base

    This class is used to define custom code base

    """

    @property
    def code(self) -> int:
        """Return code

        Returns:
            int: code

        """

        return self.value[0]

    @property
    def msg(self) -> str:
        """Return message

        Returns:
            str: message

        """

        return self.value[1]


class CustomResponseCode(CustomCodeBase):
    """Custom response code

    This class is used to define custom response code

    """

    HTTP_200 = (200, "Request successful")
    HTTP_204 = (204, "No content")
    HTTP_400 = (400, "Request failed")
    HTTP_403 = (403, "Forbidden")
    HTTP_404 = (404, "Not found")
    UNKNOWN = (999, "Unknown response code")


class CustomErrorCode(CustomCodeBase):
    """Custom error code

    This class is used to define custom error code

    """

    # Customized database error
    DB_ERROR = (1000, "Database error")
    DB_GET_DATA_ERROR = (1001, "Failed to get data from database")
    DB_ADD_DATA_ERROR = (1002, "Failed to add data to database")
    DB_UPDATE_DATA_ERROR = (1003, "Failed to update data in database")
    DB_DELETE_DATA_ERROR = (1004, "Failed to delete data from database")
