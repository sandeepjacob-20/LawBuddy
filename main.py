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

query = st.text_input("Type your legal query here...", "")

if query:
    app.agent.invoke([{"role": "user", "content": query}])