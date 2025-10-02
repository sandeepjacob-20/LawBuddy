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
        self.config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'config.yaml')
        self.chroma_persist_directory = read_config(self.config_path)['ChromaDB']['persist_directory']
        self.chroma_collection_name = read_config(self.config_path)['ChromaDB']['collection_name']
    
class LlmConfigInfo:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'llm_config.yaml')
        self.model = read_config(self.config_path)['LLM_Instructions']['Model']
        self.gemini_api_key = os.environ['gemini_api_key']

class LlmConfigInfo_LegalCaseSearch:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'llm_config.yaml')
        self.system_prompt = read_config(self.config_path)['legal_case_search']['SystemInstructions']

class LlmConfigInfo_Rephraser:
    def __init__(self):
        self.config_path = os.path.join(os.path.dirname(__file__), '..', 'configurations', 'llm_config.yaml')
        self.system_prompt = read_config(self.config_path)['rephrase_query']['SystemInstructions']
