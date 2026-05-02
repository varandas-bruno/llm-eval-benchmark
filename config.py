from pydantic_settings import BaseSettings      # use BaseSettings so it can read from .env file instead of os.getenv

class Settings(BaseSettings):
    default_provider: str = "ollama"  
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen3-7b"
    openai_api_key: str = ""
    openai_model: str = "gpt-4"
    gemini_api_key: str = ""
    gemini_model: str = "gemini-1.5-pro"

    class Config:
        env_file = ".env"                       # tells pydantic where the .env file is
        

settings = Settings()
