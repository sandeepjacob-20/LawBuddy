from lib.core.rag_retriever import RAGRetriever
from lib.core.legal_case_search import CaseLookupAI
from langgraph.graph import StateGraph, END

class Graph:
    def __init__(self):
        self.rag_retriever = RAGRetriever()
        self.case_lookup_ai = CaseLookupAI()
        