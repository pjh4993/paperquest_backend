"""This module is for base json formed dummy data.

This module contains the base json formed dummy data.

"""

from pydantic import Field, HttpUrl

from app.common.pydantic_model import ModelBase
from tests.misc import generate_random_obj_id


class BaseDummyDataFactory(ModelBase):
    """This class is for base dummy data factory.

    This class is responsible for raw json data and utility methods.

    """

    paper_metadata_id: str = Field(default_factory=generate_random_obj_id)
    paper_url: HttpUrl = Field(default="http://example.com/test.pdf")
    raw_paper_bytes: bytes = Field(default=b"test")

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
            "url": self.paper_url,
        }
