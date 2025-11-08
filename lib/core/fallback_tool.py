from langchain_core.tools import tool

@tool("fallback_tool")
def fallback_tool(query: str) -> str:
    '''
    This is a fallback tool that gets invoked when no other tools are applicable.
    It simply returns a message indicating that no specific tool could handle the query.
    Input: A general query or case description.
    Output: A message indicating fallback handling.
    '''
    print('Fallback tool invoked for query : ', query)
    return "No specific tool could handle the query. Please provide more details or rephrase your request."