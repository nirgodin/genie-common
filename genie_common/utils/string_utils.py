from difflib import SequenceMatcher


def compute_similarity_score(s1: str, s2: str) -> float:
    return SequenceMatcher(None, s1, s2).ratio()


def string_to_boolean(s: str) -> bool:
    return s.lower() == 'true'
