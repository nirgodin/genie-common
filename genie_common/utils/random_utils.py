from calendar import monthrange
from datetime import datetime
from enum import Enum
from random import choice, randint
from string import ascii_letters, digits, ascii_lowercase
from typing import Type, Optional, List, Dict

from genie_common.utils.enum_utils import get_all_enum_values


def random_alphanumeric_string(length: Optional[int] = None) -> str:
    n_chars = length or randint(0, 20)
    characters = ascii_letters + digits

    return ''.join(choice(characters) for _ in range(n_chars))


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


def random_string_array(length: Optional[int] = None) -> List[str]:
    n_elements = length or randint(0, 10)
    return [random_alphanumeric_string() for _ in range(n_elements)]


def random_integer_array(length: Optional[int] = None) -> List[int]:
    n_elements = length or randint(0, 10)
    return [randint(0, 100) for _ in range(n_elements)]


def random_lowercase_string(length: Optional[int] = None) -> str:
    n_chars = length or randint(0, 20)
    return ''.join(choice(ascii_lowercase) for _ in range(n_chars))


def random_port() -> int:
    return randint(1000, 9999)


def random_postgres_connection_url(host: str = "localhost", driver: str = "asyncpg") -> str:
    user = random_alphanumeric_string()
    password = random_alphanumeric_string()
    port = random_port()
    db_name = random_alphanumeric_string()

    return f'postgresql+{driver}://{user}:{password}@{host}:{port}/{db_name}'
