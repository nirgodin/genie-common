from functools import reduce
from typing import Any, Optional


def safe_nested_get(dct: dict, paths: list, default: Optional[Any] = None) -> Any:
    value = dct.get(paths[0], {})

    for path in paths[1:]:
        value = value.get(path, {})

    return value if value != {} else default


def merge_dicts(*dicts: Optional[dict]) -> dict:
    merged_dict = {}

    for d in dicts:
        if isinstance(d, dict):
            merged_dict.update(d)

    return merged_dict


def sort_dict_by_value(dct: dict, reverse: bool = True) -> dict:
    return dict(sorted(dct.items(), key=lambda x: x[1], reverse=reverse))


def sort_dict_by_key(dct: dict, reverse: bool = True) -> dict:
    return dict(sorted(dct.items(), key=lambda x: x[0], reverse=reverse))


def chain_dicts(*dct: dict) -> dict:
    return reduce(lambda dict1, dict2: {**dict1, **dict2}, dct)
