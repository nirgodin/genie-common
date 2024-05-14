from dataclasses import dataclass


@dataclass
class TranslationResponse:
    text: str
    translation: str
    source_language: str
    target_language: str
