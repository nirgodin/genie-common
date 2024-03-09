from calendar import monthrange
from datetime import datetime
from enum import Enum
from random import choice, randint
from string import ascii_letters, digits
from typing import Type, Optional

from genie_common.utils.enum_utils import get_all_enum_values


def random_alphanumeric_string(length: int = 32) -> str:
    characters = ascii_letters + digits
    return ''.join(choice(characters) for _ in range(length))


def random_enum_value(enum_: Type[Enum]) -> Enum:
    enum_values = get_all_enum_values(enum_)
    return choice(enum_values)


def random_boolean() -> bool:
    return choice([True, False])


def random_datetime(**kwargs) -> datetime:
    year = kwargs.get("year", randint(1950, 2023))
    month = kwargs.get("month", randint(1, 12))
    _, last_month_day = monthrange(year, month)

    return datetime(
        year=year,
        month=month,
        day=kwargs.get("day", randint(1, last_month_day)),
        hour=kwargs.get("hour", randint(0, 23)),
        minute=kwargs.get("minute", randint(0, 59)),
        second=kwargs.get("second", randint(0, 59)),
        microsecond=kwargs.get("microsecond", randint(0, 999999))
    )