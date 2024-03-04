from enum import Enum
from random import choice
from string import ascii_letters, digits
from typing import Type

from genie_common.utils.enum_utils import get_all_enum_values


def random_alphanumeric_string(length: int = 32) -> str:
    characters = ascii_letters + digits
    return ''.join(choice(characters) for _ in range(length))


def random_enum_value(enum_: Type[Enum]) -> Enum:
    enum_values = get_all_enum_values(enum_)
    return choice(enum_values)


def random_boolean() -> bool:
    return choice([True, False])
