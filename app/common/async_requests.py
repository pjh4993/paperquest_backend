# -*- coding: utf-8 -*-
"""General async requests module.

This module is used to make async requests.

"""

from contextlib import asynccontextmanager
from urllib.parse import urlparse

import aiohttp
import backoff
from pydantic import AnyHttpUrl


class AsyncRequestHandler:
    """Async request handler class.

    This class is used to handle async requests.

    """

    def __init__(self, num_connection: int = 1, timeout: int = 10):
        """Initialize async request handler class.

        Args:
            num_connection (int): The number of connection.
            timeout (int): The request timeout.

        """

        self.num_connection = num_connection
        self.timeout = timeout

    @asynccontextmanager
    async def connect_session(self, host: str):
        """Connect to the session.

        Yields:
            aiohttp.ClientSession: The client session.

        """

        session = aiohttp.ClientSession(
            base_url=host,
            connector=aiohttp.TCPConnector(limit=self.num_connection),
            timeout=aiohttp.ClientTimeout(total=self.timeout),
        )

        try:
            yield session

        finally:
            await session.close()

    async def request(self, method: str, url: AnyHttpUrl, **kwargs):
        """Make a request.

        Args:
            method (str): The request method.
            url (str): The request url.
            **kwargs: The request keyword arguments.

        Returns:
            dict: The response.

        """

        parsed_url = urlparse(str(url))

        if not parsed_url.hostname or not parsed_url.path:
            raise ValueError("Invalid url")

        async with self.connect_session(parsed_url.hostname) as session:
            return await self._request(
                session=session, method=method, url=parsed_url.path, **kwargs
            )

    @backoff.on_exception(
        backoff.expo,
        aiohttp.ClientError,
        max_tries=3,
        factor=2,
        logger=None,
    )
    async def _request(self, session: aiohttp.ClientSession, method: str, url: str, **kwargs):
        """Make a request.

        Args:
            session (aiohttp.ClientSession): The client session.
            method (str): The request method.
            url (str): The request url.
            **kwargs: The request keyword arguments.

        Returns:
            dict: The response.

        """

        async with session.request(method=method, url=url, **kwargs) as response:
            response.raise_for_status()

            return response
