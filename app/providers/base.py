class BaseProvider:
    def __init__(self, config):
        self.config = config

    def generate(self, prompt: str) -> str:
        raise NotImplementedError("Subclasses must implement this method")