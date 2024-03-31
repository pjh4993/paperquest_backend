"""Application wise enums

This module contains the application wise enums.

"""

from enum import IntEnum


class BackgroundTaskStatus(IntEnum):
    """Background task status enum.

    This class is responsible for background task status enum.

    """

    IN_PROGRESS = 0  # Background task is in progress.
    SUCCESS = 1  # Background task is success.
    FAILED = 2  # Background task is failed.
