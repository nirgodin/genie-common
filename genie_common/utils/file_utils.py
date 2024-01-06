import json

from genie_common.consts import UTF_8
from genie_common.typing import Json


def to_json(json_: Json, path: str) -> None:
    with open(path, 'w', encoding=UTF_8) as f:
        json.dump(json_, f, ensure_ascii=False, indent=4)


def read_json(path: str) -> Json:
    with open(path, 'r', encoding=UTF_8) as f:
        return json.load(f)
