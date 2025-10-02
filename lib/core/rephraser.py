from google import genai
from google.genai import types
from lib.utils.config_reader import LlmConfigInfo, LlmConfigInfo_Rephraser
import json

class Rephraser:
    def __init__(self, model: str):
        llm_config = LlmConfigInfo
        rephraser_config = LlmConfigInfo_Rephraser
        self.client = genai.Client(api_key=llm_config.gemini_api_key)
        self.config = types.GenerateContentConfig(
            system_instruction=rephraser_config.system_prompt
        )
        self.model = llm_config.model

    def rephrase_query(self, user_input: str) -> str:
        '''
        This tool rephrases a given user query to make it more precise and contextually relevant in legal terms.
        Input: A legal query or description of a case.
        Output: A rephrased version of the input query focusing on the legal phrases.
        '''
        response = self.client.models.generate_content(
                model=self.model,
                contents=user_input,
                config=self.config
            )
        try:
            response_json = response.text[(response.text.index("```json")+ len("```json")):response.text.rindex("```")].strip()
        except Exception as e:
            print("Error parsing response to JSON:", e)
            response_json = '{"error": "Failed to parse response to JSON."}'

        return json.loads(response_json)