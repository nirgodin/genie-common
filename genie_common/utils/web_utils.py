from ssl import create_default_context
from typing import Optional

from aiohttp import ClientResponse, ClientResponseError, ClientSession, TCPConnector, CookieJar
from certifi import where

from genie_common.tools import logger
from genie_common.typing import Json


async def jsonify_response(raw_response: ClientResponse, wrap_exceptions: bool = True) -> Optional[Json]:
    try:
        raw_response.raise_for_status()
        return await raw_response.json()

    except ClientResponseError:
        if wrap_exceptions:
            logger.exception(f"Received exception while jsonifying response. Returning None instead.")
        else:
            raise


async def fetch_image(session: ClientSession, url: str, wrap_exceptions: bool = True) -> bytes:
    try:
        async with session.get(url) as raw_response:
            raw_response.raise_for_status()
            return await raw_response.read()

    except ClientResponseError:
        if wrap_exceptions:
            logger.exception(f"Received exception while fetching image. Returning None instead.")
        else:
            raise


def create_client_session(headers: Optional[dict] = None) -> ClientSession:
    ssl_context = create_default_context(cafile=where())
    return ClientSession(
        connector=TCPConnector(ssl=ssl_context),
        cookie_jar=CookieJar(quote_cookie=False),
        headers=headers
    )
