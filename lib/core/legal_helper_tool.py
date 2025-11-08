from langchain_core.tools import tool
from lib.core.rag_retriever import RAGRetriever
from lib.core.legal_case_search import CaseLookupAI
from lib.core.rephraser import Rephraser

@tool("legal_helper")
def legal_helper(query: str) -> str:
    '''
    This tool combines the functionalities of RAG Retriever, Case Lookup AI, and Rephraser to provide comprehensive legal assistance.
    It takes the user input, rephrases the query to make it more precise and contextually relevant in legal terms then finds the legal provisions from the Bharatiya Nyaya Sanhita (BNS),
    and finally looks up similar cases from the past on the internet.  
    Input: A legal query or case description.
    Output: A JSON object containing relevant legal document sections, similar cases with their details.
    '''
    print('Tool invoked for query : ',query)
    try:
        rephrased_query = Rephraser().rephrase_query(query)['rephrased_query']
        print("**********STATUS UPDATE**************\nRephrasing completed.")
        retrieved_docs = RAGRetriever().rag_retriever(rephrased_query)
        print("**********STATUS UPDATE**************\nRAG retrieval completed.")
        case_lookup_results = CaseLookupAI().get_case_lookup(rephrased_query)
        print("**********STATUS UPDATE**************\nCase lookup completed.")
    except Exception as e:
        print("Error in legal_helper tool:", e)
        return {"error": str(e)}
    
    result = {
        "relevant BNS sections": retrieved_docs,
        "Past similar case information": case_lookup_results
    }
    print('result:', result)
    
    return result