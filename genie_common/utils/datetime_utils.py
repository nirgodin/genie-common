from datetime import datetime
from typing import Optional, List

from genie_common.tools import logger


def to_datetime(date_time: str, formats: List[str]) -> Optional[datetime]:
    for format_ in formats:
        try:
            return datetime.strptime(date_time, format_)
        except:
            logger.warning(f"Could not parse `{date_time}` to datetime using this format `{format_}`. Trying next.")

    logger.warning(f"Could not parse `{date_time}` to datetime using any of the supplied. Returning None instead.")
