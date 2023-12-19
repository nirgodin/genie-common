from difflib import SequenceMatcher


def compute_similarity_score(s1: str, s2: str) -> float:
    return SequenceMatcher(None, s1, s2).ratio()


def string_to_boolean(s: str) -> bool:
    return s.lower() == 'true'


def contains_any_hebrew_character(s: str) -> bool:
    return any("\u0590" <= char <= "\u05EA" for char in s)
