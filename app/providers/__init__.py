from ollama_provider import OllamaProvider
from openai_provider import OpenAIProvider

def build_provider(provider_name: str):
    '''
    Factory function to build the appropriate provider based on the provider name.
    Args:
        provider_name (str): The name of the provider to build (e.g., "ollama", "openai").
    Returns:
        An instance of the specified provider class.
    Raises:
        ValueError: If the provider name is not supported.
    '''
    
    if provider_name == "ollama":
        return OllamaProvider
    elif provider_name == "openai":
        return OpenAIProvider
    else:
        raise ValueError(f"Unsupported provider: {provider_name}")
    
    
    