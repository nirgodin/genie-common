from abc import ABC, abstractmethod
from typing import Any


class IEncoder(ABC):
    @abstractmethod
    def encode(self, obj: Any) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def decode(self, obj: Any) -> Any:
        raise NotImplementedError()
