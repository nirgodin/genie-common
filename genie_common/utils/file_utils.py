import json
from typing import List

from genie_common.consts import UTF_8
from genie_common.typing import Json


def to_json(json_: Json, path: str) -> None:
    with open(path, 'w', encoding=UTF_8) as f:
        json.dump(json_, f, ensure_ascii=False, indent=4)


def read_json(path: str) -> Json:
    with open(path, 'r', encoding=UTF_8) as f:
        return json.load(f)


def to_jsonl(records: List[dict], path: str) -> None:
    with open(path, "w", encoding=UTF_8) as file:
        for record in records:
            json_str = json.dumps(record)
            file.write(json_str + "\n")


def read_jsonl(data: str) -> List[dict]:
    records = []

    for line in data.split("\n"):
        if line != "":
            record = json.loads(line)
            records.append(record)

    return records
