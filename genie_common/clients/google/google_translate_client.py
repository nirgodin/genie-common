from typing import Optional, List

from google.cloud.translate_v3 import TranslationServiceClient
from google.oauth2.service_account import Credentials

from genie_common.models.google import TranslationResponse
from genie_common.utils import load_google_service_account_info, run_async, get_google_project_id


class GoogleTranslateClient:
    def __init__(self, translation_service: TranslationServiceClient, parent: str):
        self._translation_service = translation_service
        self._parent = parent

    @classmethod
    def create(cls) -> "GoogleTranslateClient":
        service_account_info = load_google_service_account_info()
        credentials = Credentials.from_service_account_info(service_account_info)
        translation_service = TranslationServiceClient(credentials=credentials)
        project_id = get_google_project_id(service_account_info)

        return cls(translation_service, f"projects/{project_id}")

    async def translate(self,
                        texts: List[str],
                        target_language: str,
                        source_language: Optional[str] = None) -> List[TranslationResponse]:
        return await run_async(lambda: self.translate_sync(texts, target_language, source_language))

    def translate_sync(self,
                       texts: List[str],
                       target_language: str,
                       source_language: Optional[str] = None) -> List[TranslationResponse]:
        response = self._translation_service.translate_text(
            parent=self._parent,
            contents=texts,
            source_language_code=source_language,
            target_language_code=target_language,
        )
        translations = []

        for text, translate_response in zip(texts, response.translations):
            translation_response = TranslationResponse(
                text=text,
                translation=translate_response.translated_text,
                source_language=source_language or translate_response.detected_language_code,
                target_language=target_language
            )
            translations.append(translation_response)

        return translations
