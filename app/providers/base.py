from abc import ABC, abstractmethod

# Create an abstract base class to ensure that all providers implement the same methods
class BaseProvider(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")