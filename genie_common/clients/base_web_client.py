from abc import ABC, abstractmethod
from typing import Any, Optional

from aiohttp import ClientSession

from genie_common.tools import logger
from genie_common.typing import Json
from genie_common.clients.utils import jsonify_response


class BaseWebClient(ABC):
    def __init__(self, session: ClientSession, base_url: str, wrap_exceptions: bool = True):
        self._session = session
        self._base_url = base_url
        self._wrap_exceptions = wrap_exceptions

    async def collect(self, *args, **kwargs) -> Optional[Any]:
        logger.info(f"Starting collect data from OpenAI `{self._route}` endpoint")
        body = self._build_request_body(*args, **kwargs)
        response = await self._post(body)

        if response is not None:
            serialized_response = self._serialize_response(response)
            logger.info(f"Successfully collected data from OpenAI `{self._route}` endpoint")

            return serialized_response

    @abstractmethod
    def _build_request_body(self, *args, **kwargs) -> dict:
        raise NotImplementedError

    @abstractmethod
    def _serialize_response(self, response: Json) -> Any:
        raise NotImplementedError

    async def _post(self, body: dict) -> Optional[Json]:
        async with self._session.post(url=self._url, json=body) as raw_response:
            return await jsonify_response(raw_response, self._wrap_exceptions)

    @property
    @abstractmethod
    def _route(self) -> str:
        raise NotImplementedError

    @property
    def _url(self) -> str:
        return f"{self._base_url}/{self._route}"
