import json
from typing import Optional

from genie_common.models.openai import ImageSize
from genie_common.openai.base_openai_collector import BaseOpenAICollector
from genie_common.openai.openai_consts import SIZE, N, PROMPT, RESPONSE_FORMAT, B64_JSON, DATA, IMAGE
from genie_common.typing import Json


class ImageGeneratorCollector(BaseOpenAICollector):
    def _build_request_body(self, prompt: str, n: int, size: ImageSize) -> dict:
        return {
            PROMPT: prompt,
            N: 1,
            SIZE: size.value,
            RESPONSE_FORMAT: B64_JSON
        }

    def _serialize_response(self, response: Json) -> Optional[str]:
        data = response[DATA]

        if data:
            serialized_response = json.loads(data[0])
            return serialized_response[IMAGE]

    @property
    def _route(self) -> str:
        return "images/generations"
