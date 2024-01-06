from typing import Any


def is_primitive(obj: Any) -> bool:
    return isinstance(obj, (bool, str, int, float, type(None)))
