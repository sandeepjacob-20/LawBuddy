from typing import Literal
from langgraph.prebuilt import ToolNode
from lib.core.legal_helper_tool import legal_helper
from lib.core.fallback_tool import fallback_tool
from langgraph.graph import StateGraph, END, MessagesState
from lib.core.ollama import OllamaClient
from langgraph.checkpoint.memory import MemorySaver
from langchain.schema import AIMessage


class Graph:
    def __init__(self):
        self.tools = [legal_helper.func, fallback_tool.func]
        self.tool_node = ToolNode(self.tools)
        self.client = OllamaClient(tools=self.tools).client
        # self.client = OllamaClient().client
        self.checkpointer = MemorySaver()
        self.agent = self.create_workflow()

    def should_continue(self, state: MessagesState) -> Literal["Tools", END]:
        messages = state['messages']
        last_message = messages[-1]

        if isinstance(last_message, AIMessage) and last_message.tool_calls:
            print("Tool calls made:", last_message.tool_calls)
            return "Tools"
        
        print("No tool calls made. Ending the workflow.")
        return END
    
    def call_model(self, state: MessagesState):
        messages = state['messages']

        model = self.client
        try:
            response = model.invoke(messages)
            state["messages"].append(response)
            return state
        except Exception as e:
            print("Error during model invocation:", e)
            return {'messages': []}
        
    def create_workflow(self):
        
        workflow = StateGraph(MessagesState)

        workflow.add_node('agent', self.call_model)
        workflow.add_node('Tools', self.tool_node)

        workflow.set_entry_point('agent')
        workflow.add_conditional_edges('agent',self.should_continue)
        workflow.add_edge('Tools', 'agent')

        app = workflow.compile(
            checkpointer=self.checkpointer
        )

        app.get_graph() .print_ascii()

        return app

