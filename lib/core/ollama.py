from langchain_ollama import ChatOllama
from lib.utils.config_reader import LlmConfigInfo

class OllamaClient:
    def __init__(self, tools: list = []):
        llm_config = LlmConfigInfo()
        self.client = ChatOllama(model=llm_config.chat_model).bind(tools=tools) 
        # self.client = ChatOllama(model=llm_config.chat_model)