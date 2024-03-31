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

    def __init__(self):
        """Initialize the base dummy data factory.

        This method is used to initialize the base dummy data factory.

        """

        self.paper_metadata_id = self.generate_random_obj_id()

    @property
    def paper_metadata_json(self) -> dict:
        """Get the paper metadata.

        This method is responsible for getting the paper metadata.

        Returns:
            dict: The paper metadata.

        """

        return {
            "_id": self.paper_metadata_id,
            "title": "title",
            "authors": ["author1", "author2"],
            "abstract": "abstract",
            "published_at": "2021-01-01T00:00:00",
            "venue": "venue",
            "keywords": ["keyword1", "keyword2"],
            "url": "http://example.com/test.pdf",
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
