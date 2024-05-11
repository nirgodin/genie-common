from typing import Union, Dict, List, Optional

from genie_common.clients.openai.openai_collectors.base_openai_collector import BaseOpenAICollector
from genie_common.clients.openai.openai_consts import MODEL, MESSAGES, CHOICES, CONTENT, MESSAGE
from genie_common.models.openai import ChatCompletionsModel
from genie_common.utils import safe_nested_get


class ChatCompletionsCollector(BaseOpenAICollector):
    def _serialize_response(self, response: Union[dict, list]) -> Optional[str]:
        choices = response.get(CHOICES)

        if choices:
            first_choice = choices[0]
            return safe_nested_get(first_choice, [MESSAGE, CONTENT])

    def _build_request_body(self, messages: List[Dict[str, str]], model: ChatCompletionsModel) -> dict:
        return {
            MODEL: model.value,
            MESSAGES: messages
        }

    @property
    def _route(self) -> str:
        return "chat/completions"
