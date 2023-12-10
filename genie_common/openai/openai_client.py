from aiohttp import ClientSession

from genie_common.openai.openai_collectors import ChatCompletionsCollector, EmbeddingsCollector, ImageGeneratorCollector
from genie_common.openai.openai_collectors.images_variator_collector import ImageVariatorCollector


class OpenAIClient:
    def __init__(self,
                 chat_completions: ChatCompletionsCollector,
                 embeddings: EmbeddingsCollector,
                 images_generation: ImageGeneratorCollector,
                 images_variation: ImageVariatorCollector):
        self.chat_completions = chat_completions
        self.embeddings = embeddings
        self.images_generation = images_generation
        self.images_variation = images_variation

    @classmethod
    def create(cls, session: ClientSession, wrap_exceptions: bool = True) -> "OpenAIClient":
        return cls(
            chat_completions=ChatCompletionsCollector(session, wrap_exceptions),
            embeddings=EmbeddingsCollector(session, wrap_exceptions),
            images_generation=ImageGeneratorCollector(session, wrap_exceptions),
            images_variation=ImageVariatorCollector(session, wrap_exceptions)
        )
