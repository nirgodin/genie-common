from abc import ABC, abstractmethod
from typing import Any, Union

from aiohttp import ClientSession

from genie_common.openai.openai_consts import BASE_OPENAI_API_URL
from genie_common.tools import logger


class BaseOpenAICollector(ABC):
    def __init__(self, session: ClientSession):
        self._session = session

    async def collect(self, *args, **kwargs) -> Any:
        logger.info(f"Starting collect data from OpenAI `{self._route}` endpoint")
        body = self._build_request_body(*args, **kwargs)
        response = await self._post(body)
        serialized_response = self._serialize_response(response)
        logger.info(f"Successfully collected data from OpenAI `{self._route}` endpoint")

        return serialized_response

    @abstractmethod
    def _build_request_body(self, *args, **kwargs) -> dict:
        raise NotImplementedError

    @abstractmethod
    def _serialize_response(self, response: Union[dict, list]) -> Any:
        raise NotImplementedError

    async def _post(self, body: dict) -> Union[dict, list]:
        async with self._session.post(url=self._url, json=body) as raw_response:
            raw_response.raise_for_status()
            return await raw_response.json()

    @property
    @abstractmethod
    def _route(self) -> str:
        raise NotImplementedError

    @property
    def _url(self) -> str:
        return BASE_OPENAI_API_URL
