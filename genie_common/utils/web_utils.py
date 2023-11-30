from typing import Optional

from aiohttp import ClientResponse, ClientResponseError

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
