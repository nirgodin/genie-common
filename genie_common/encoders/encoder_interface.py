from abc import ABC, abstractmethod
from typing import Any


class IEncoder(ABC):
    @staticmethod
    @abstractmethod
    def encode(obj: Any) -> Any:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def decode(obj: Any) -> Any:
        raise NotImplementedError()
