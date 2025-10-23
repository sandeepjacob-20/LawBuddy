import streamlit as st
from lib.core.graph import Graph

app = Graph()

st.set_page_config(page_title="Law Buddy", page_icon="⚖️", layout="centered")

# # Minimalistic styling
# st.markdown(
#     """
#     <style>
#     .main {background-color: #f9f9f9;}
#     .stTextInput>div>div>input {
#         border-radius: 8px;
#         border: 1px solid #ccc;
#         padding: 10px;
#         font-size: 18px;
#     }
#     .stHeadingWithActionElements>h1 {
#         font-size: 300px;
#         color: #333;
#         margin-bottom: 20px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

st.title("Law Buddy")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        'role': "assistant",
        'content': "Hello! I'm Law Buddy, your AI-powered legal assistant. How can I assist you today?"
    }]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your legal query here..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})    


    response = app.agent.invoke(
            {"messages": st.session_state.messages},
            config={"configurable": {"thread_id": "lawbuddy-session-1"}}
        )
    # Display assistant response in chat message container
    assistant_message = response['messages'][-1].content
    st.chat_message("assistant").markdown(assistant_message)
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})

# query = st.text_input("Type your legal query here...", "")

# if query:
#     response = app.agent.invoke(
#     {"messages": [{"role": "user", "content": "Hello"}]},
#     config={"configurable": {"thread_id": "lawbuddy-session-1"}}
# )
#     print(response)