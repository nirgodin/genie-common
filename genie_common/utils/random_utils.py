from random import choice
from string import ascii_letters, digits


def random_alphanumeric_string(length: int = 32) -> str:
    characters = ascii_letters + digits
    return ''.join(choice(characters) for _ in range(length))
