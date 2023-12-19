import re
from typing import List


def search_between_two_characters(start_char: str, end_char: str, text: str) -> List[str]:
    return re.findall(f"{start_char}(.*?){end_char}", text)
