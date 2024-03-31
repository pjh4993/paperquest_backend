"""This module is for base json formed dummy data.

This module contains the base json formed dummy data.

"""

import binascii
import os
import time


class BaseDummyDataFactory:
    """This class is for base dummy data factory.

    This class is responsible for raw json data and utility methods.

    """

    @property
    def paper_metadata_json(self) -> dict:
        """Get the paper metadata.

        This method is responsible for getting the paper metadata.

        Returns:
            dict: The paper metadata.

        """

        return {
            "title": "title",
            "authors": ["author1", "author2"],
            "abstract": "abstract",
            "published_at": "2021-01-01T00:00:00",
            "venue": "venue",
            "keywords": ["keyword1", "keyword2"],
        }

    @staticmethod
    def generate_random_obj_id() -> str:
        """Generate random object id

        Generate random object id with timestamp and random string

        Returns:
            str : random object id

        """

        timestamp = int(time.time())
        rest = binascii.b2a_hex(os.urandom(8)).decode("ascii")
        return f"{timestamp:x}{rest}"
