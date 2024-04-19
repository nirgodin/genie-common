from abc import ABC, abstractmethod
from typing import Optional

from aiohttp import ClientSession

from genie_common.clients.utils import jsonify_response
from genie_common.typing import Json


class BaseWebClient(ABC):
    def __init__(self, session: ClientSession, base_url: str, wrap_exceptions: bool = True):
        self._session = session
        self._base_url = base_url
        self._wrap_exceptions = wrap_exceptions

    async def _get(self, params: Optional[dict] = None) -> Json:
        async with self._session.get(url=self._url, params=params) as raw_response:
            raw_response.raise_for_status()
            return await jsonify_response(raw_response, self._wrap_exceptions)

    async def _post(self, payload: dict) -> Json:
        async with self._session.post(url=self._url, json=payload) as raw_response:
            raw_response.raise_for_status()
            return await jsonify_response(raw_response, self._wrap_exceptions)

    @property
    @abstractmethod
    def _route(self) -> str:
        raise NotImplementedError

    @property
    def _url(self) -> str:
        return f"{self._base_url}/{self._route}"
