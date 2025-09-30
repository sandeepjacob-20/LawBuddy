from google.genai import types
from langchain_core.tools import tool
from google import genai
import json
from lib.utils.config_reader import LlmConfigInfo, LlmConfigInfo_LegalCaseSearch

class CaseLookupAI:
    def __init__(self):
        llm_config = LlmConfigInfo()
        llm_lookup_config = LlmConfigInfo_LegalCaseSearch()
        self.client = genai.Client(api_key=llm_config.gemini_api_key)
        grounding_tool = types.Tool(
            google_search=types.GoogleSearch()
        )
        self.config = types.GenerateContentConfig(
            tools=[grounding_tool],
            system_instruction=llm_lookup_config.system_prompt
        )
        self.model = llm_config.model

    @tool
    def get_case_lookup(self, user_input: str) -> str:
        '''
        This tool looks up similar cases from the past on the internet along with its judgement and other information.
        Input: A legal query or case description.
        Output: A JSON object containing a list of similar cases with their details.
        '''
        response = self.client.models.generate_content(
                model=self.model,
                contents=user_input,
                config=self.config,
            )
        try:
            respone_json = response.text[(response.text.index("```json")+ len("```json")):response.text.rindex("```")].strip()
        except Exception as e:
            print("Error parsing response to JSON:", e)
            respone_json = '{"error": "Failed to parse response to JSON."}'
            
        return json.loads(respone_json)