import ollama
from config import settings

class OllamaProvider:
    
    def __init__(self): 
        # both from config file
        self.model = settings.ollama_model
        self.base_url = settings.ollama_base_url
        
    def call_llm(self, prompt):
        
        # make the call to the llm and returns the response
        response = ollama.chat(
            model=self.model,
            messages=[{
                "role":"system",
                "content":prompt
            }]
        )
        
        return response["message"]["content"]
    