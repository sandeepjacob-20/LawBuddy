import yaml
import os

def read_config(config_path: str) -> dict:
        """
        Reads a YAML configuration file and returns its contents as a dictionary.
        """
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file '{config_path}' not found.")
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config

class ConfigInfo:
    def __init__(self):
        self.config_path = '../configurations/config.yaml'
        self.chroma_persist_directory = read_config(self.config_path)['ChromaDB']['persist_directory']
        self.chroma_collection_name = read_config(self.config_path)['ChromaDB']['collection_name']
    
class LlmConfigInfo:
    def __init__(self):
        self.config_path = '../configurations/llm_config.yaml'
        self.model = self.read_config(self.config_path)['LLM_Instructions']['model']
        self.gemini_api_key = os.environ['gemini_api_key']

class LlmConfigInfo_LegalCaseSearch:
    def __init__(self):
        self.config_path = '../configurations/llm_config.yaml'
        self.system_prompt = self.read_config(self.config_path)['legal_case_search']['SystemInstructions']
