import re
from typing import List, Optional


def search_between_two_characters(start_char: str, end_char: str, text: str) -> List[str]:
    return re.findall(f"{start_char}(.*?){end_char}", text)


def extract_int_from_string(s: str) -> Optional[int]:
    all_numeric_string = re.sub(r'[^0-9]', '', s)

    if all_numeric_string != "":
        return int(all_numeric_string)


def sub_between_two_characters(start_char: str, end_char: str, repl: str, text: str) -> str:
    return re.sub(rf"{start_char}.*?{end_char}", repl, text)


def sub_all_chars_before(chars: List[str], text: str) -> str:
    joined_chars = "".join(chars)
    pattern = rf"^.*?[{joined_chars}]"

    return re.sub(pattern, "", text)
