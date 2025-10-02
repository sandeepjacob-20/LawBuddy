from langchain_core.tools import tool
from lib.core.rag_retriever import RAGRetriever
from lib.core.legal_case_search import CaseLookupAI
from lib.core.rephraser import Rephraser

class LegalHelperTool:
    def __init__(self):
        self.rag_retriever = RAGRetriever.rag_retriever  
        self.case_lookup = CaseLookupAI.get_case_lookup
        self.rephraser = Rephraser.rephrase_query
    
    @tool
    def legal_helper(self, query: str) -> str:
        '''
        This tool combines the functionalities of RAG Retriever, Case Lookup AI, and Rephraser to provide comprehensive legal assistance.
        It takes the user input, rephrases the query to make it more precise and contextually relevant in legal terms then finds the legal provisions from the Bharatiya Nyaya Sanhita (BNS),
        and finally looks up similar cases from the past on the internet.  
        Input: A legal query or case description.
        Output: A JSON object containing relevant legal document sections, similar cases with their details.
        '''
        rephrased_query = self.rephraser(query)['rephrased_query']
        retrieved_docs = self.rag_retriever(rephrased_query)
        case_lookup_results = self.case_lookup(rephrased_query)
        
        result = {
            "relevant BNS sections": retrieved_docs,
            "Past similar case information": case_lookup_results
        }
        
        return result