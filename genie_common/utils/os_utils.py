import os
from typing import List, Optional

from genie_common.tools import logger


def is_empty_dir(dir_path: str) -> bool:
    dir_files = os.listdir(dir_path)
    return len(dir_files) == 0


def env_var_to_bool(key: str, default: bool = False) -> bool:
    var = os.getenv(key)

    if var is None:
        logger.warn(f"Requested to get boolean value of var `{key}` but variable is missing. Returning default value")
        return default

    return var.lower() == "true"


def env_var_to_int(key: str, default: int = 0) -> int:
    var = os.getenv(key)

    if var is None:
        logger.warn(f"Requested to get integer value of var `{key}` but variable is missing. Returning default value")
        return default

    try:
        return int(var)

    except ValueError:
        logger.exception(f"Requested to get value of var `{key}` but var is not of type int. Returning default value")
        return default


def env_var_to_list(key: str, sep: str = ",", default: Optional[List[str]] = None) -> List[str]:
    var = os.getenv(key)

    if var is None:
        logger.warn(f"Requested to get list value of var `{key}` but variable is missing. Returning default value")
        return default or []

    return [elem.strip() for elem in var.split(sep)]
