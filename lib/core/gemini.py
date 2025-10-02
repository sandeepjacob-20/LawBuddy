from langchain_google_genai import ChatGoogleGenerativeAI
from lib.utils.config_reader import LlmConfigInfo

class GeminiClient:
    def __init__(self, tools: list = []):
        llm_config = LlmConfigInfo()
        self.client = ChatGoogleGenerativeAI(model=llm_config.model).bind(tools=tools)