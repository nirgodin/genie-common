from calendar import monthrange
from datetime import datetime
from typing import Optional, List

from genie_common.consts import DEFAULT_DATETIME_FORMAT
from genie_common.tools import logger


def to_datetime(date_time: str, formats: List[str]) -> Optional[datetime]:
    for format_ in formats:
        try:
            return datetime.strptime(date_time, format_)
        except ValueError:
            logger.debug(f"Could not parse `{date_time}` to datetime using this format `{format_}`. Trying next.")

    logger.warning(f"Could not parse `{date_time}` to datetime using any of the supplied. Returning None instead.")


def from_datetime(date_time: datetime, format_: str = DEFAULT_DATETIME_FORMAT) -> str:
    return date_time.strftime(format_)


def get_last_month_day(date_time: datetime) -> int:
    _, day = monthrange(date_time.year, date_time.month)
    return day
