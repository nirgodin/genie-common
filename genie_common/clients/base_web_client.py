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

    async def _get(self, params: Optional[dict] = None, route: Optional[str] = None) -> Json:
        url = self._build_url(route)

        async with self._session.get(url=url, params=params) as raw_response:
            raw_response.raise_for_status()
            return await jsonify_response(raw_response, self._wrap_exceptions)

    async def _post(self, payload: dict, route: Optional[str] = None) -> Json:
        url = self._build_url(route)

        async with self._session.post(url=url, json=payload) as raw_response:
            raw_response.raise_for_status()
            return await jsonify_response(raw_response, self._wrap_exceptions)

    def _build_url(self, route: Optional[str]) -> str:
        if route is None:
            return self._url

        return f"{self._url}/{route}"

    @property
    @abstractmethod
    def _route(self) -> str:
        raise NotImplementedError

    @property
    def _url(self) -> str:
        return f"{self._base_url}/{self._route}"
