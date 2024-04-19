from abc import ABC, abstractmethod
from typing import Optional, Any

from aiohttp import ClientSession

from genie_common.clients import BaseWebClient
from genie_common.clients.openai.openai_consts import BASE_OPENAI_API_URL
from genie_common.typing import Json


class BaseOpenAICollector(BaseWebClient, ABC):
    def __init__(self, session: ClientSession, wrap_exceptions: bool = True):
        super().__init__(
            session=session,
            base_url=BASE_OPENAI_API_URL,
            wrap_exceptions=wrap_exceptions
        )

    async def collect(self, *args, **kwargs) -> Optional[Any]:
        body = self._build_request_body(*args, **kwargs)
        response = await self._post(body)

        if response is not None:
            serialized_response = self._serialize_response(response)

            return serialized_response

    @abstractmethod
    def _build_request_body(self, *args, **kwargs) -> dict:
        raise NotImplementedError

    @abstractmethod
    def _serialize_response(self, response: Json) -> Any:
        raise NotImplementedError
