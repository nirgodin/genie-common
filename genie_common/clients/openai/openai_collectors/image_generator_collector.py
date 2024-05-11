from typing import Optional

from genie_common.clients.openai.openai_collectors.base_openai_collector import BaseOpenAICollector
from genie_common.clients.openai.openai_consts import SIZE, N, PROMPT, RESPONSE_FORMAT, B64_JSON, DATA, MODEL
from genie_common.models.openai import ImageSize, DallEModel
from genie_common.typing import Json


class ImageGeneratorCollector(BaseOpenAICollector):
    def _build_request_body(self, prompt: str, n: int, size: ImageSize, model: DallEModel) -> dict:
        return {
            PROMPT: prompt,
            N: 1,
            SIZE: size.value,
            RESPONSE_FORMAT: B64_JSON,
            MODEL: model.value
        }

    def _serialize_response(self, response: Json) -> Optional[str]:
        data = response[DATA]

        if data:
            return data[0][B64_JSON]

    @property
    def _route(self) -> str:
        return "images/generations"
