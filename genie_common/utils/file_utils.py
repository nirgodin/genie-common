import json

from genie_common.typing import Json


def to_json(json_: Json, path: str) -> None:
    with open(path, 'w', encoding="utf-8") as f:
        json.dump(json_, f, ensure_ascii=False, indent=4)


def read_json(path: str) -> Json:
    with open(path, 'r', encoding="utf-8") as f:
        return json.load(f)
