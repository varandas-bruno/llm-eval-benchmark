from openai import OpenAI
from config import settings

class OpenAIProvider:
    
    def __init__(self):
        
        self.model = settings.openai_model
        self.api_key = settings.openai_api_key
        
        
    def call_llm(self, prompt):
        
        client = OpenAI(api_key=self.api_key)
        response = client.responses.create(
            model=self.model,
            input=prompt
        )
        
        return response.output_text