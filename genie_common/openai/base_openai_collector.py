from abc import ABC


class BaseOpenAICollector(ABC):
    async def collect(self):
        pass
