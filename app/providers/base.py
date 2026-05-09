from abc import ABC, abstractmethod

class BaseProvider(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")