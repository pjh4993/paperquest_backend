"""Custom exception classes for the application.

This module contains custom exception classes for the application.

"""


class PaperQuestException(Exception):
    """Base exception class of paper quest backend.

    This class represents a base exception.

    """

    def __init__(self, message: str):
        """Initialize the base exception class.

        Args:
            message (str): The error message.

        """

        super().__init__(message)


class NotFoundError(PaperQuestException):
    """Not found error class.

    This class represents a not found error.

    """
