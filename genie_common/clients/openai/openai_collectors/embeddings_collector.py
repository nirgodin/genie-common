from typing import List, Optional

from genie_common.clients.openai.openai_collectors.base_openai_collector import BaseOpenAICollector
from genie_common.clients.openai.openai_consts import DATA, EMBEDDING, INPUT, MODEL
from genie_common.models.openai import EmbeddingsModel
from genie_common.typing import Json


class EmbeddingsCollector(BaseOpenAICollector):
    def _build_request_body(self, text: str, model: EmbeddingsModel) -> dict:
        return {
            INPUT: text,
            MODEL: model.value
        }

    def _serialize_response(self, response: Json) -> Optional[List[float]]:
        data = response.get(DATA)

        if data:
            first_element = data[0]
            return first_element.get(EMBEDDING)

    @property
    def _route(self) -> str:
        return "embeddings"
