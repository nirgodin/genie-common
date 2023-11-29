from aiohttp import ClientSession

from genie_common.openai.openai_collectors import ChatCompletionsCollector, EmbeddingsCollector, ImageGeneratorCollector


class OpenAIClient:
    def __init__(self,
                 chat_completions: ChatCompletionsCollector,
                 embeddings: EmbeddingsCollector,
                 images_generation: ImageGeneratorCollector):  # TODO: Add images variations
        self.chat_completions = chat_completions
        self.embeddings = embeddings
        self.images_generation = images_generation

    @classmethod
    def create(cls, session: ClientSession, wrap_exceptions: bool = True) -> "OpenAIClient":
        return cls(
            chat_completions=ChatCompletionsCollector(session, wrap_exceptions),
            embeddings=EmbeddingsCollector(session, wrap_exceptions),
            images_generation=ImageGeneratorCollector(session, wrap_exceptions)
        )
