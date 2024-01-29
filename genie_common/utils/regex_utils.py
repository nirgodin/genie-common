import re
from typing import List, Optional


def search_between_two_characters(start_char: str, end_char: str, text: str) -> List[str]:
    return re.findall(f"{start_char}(.*?){end_char}", text)


def extract_int_from_string(s: str) -> Optional[int]:
    all_numeric_string = re.sub(r'[^0-9]', '', s)

    if all_numeric_string != "":
        return int(all_numeric_string)
