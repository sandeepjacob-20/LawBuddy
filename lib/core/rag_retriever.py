import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain_google_genai import ChatGoogleGenerativeAI
from lib.utils.config_reader import ConfigInfo, LlmConfigInfo

class RAGRetriever:

    def __init__(self):
        self.attribute_info = [
            AttributeInfo(name="chapter_number", description="The chapter number in the BNS.", type="integer"),
            AttributeInfo(name="chapter_name", description="The name of the chapter in the BNS.", type="string"),
            AttributeInfo(name="chapter_subtype", description="The subtype of the chapter in the BNS.", type="string"),
            AttributeInfo(name="section_number", description="The specific section number of the offense.", type="integer"),
            AttributeInfo(name="section_name", description="The name of the section or a brief summary of the offense.", type="string"),
        ]
        self.document_content_description = "A section from the Bharatiya Nyaya Sanhita (BNS) describing a criminal offense, ist BNS section, its definition, and its punishment."
        llm_config = LlmConfigInfo()
        self.llm = ChatGoogleGenerativeAI(model=llm_config.model)
        self.model_name = "sentence-transformers/all-MiniLM-L6-v2"
        self.embeddings = HuggingFaceEmbeddings(model_name=self.model_name)
        config = ConfigInfo()
        persist_directory = os.path.join(os.path.dirname(__file__), '..', config.chroma_persist_directory)
        self.vectorstore = Chroma(persist_directory=persist_directory, embedding_function=self.embeddings,collection_name=config.chroma_collection_name)

    def rag_retriever(self, query: str):
        '''
        This tool retrieves relevant sections from the Bharatiya Nyaya Sanhita (BNS) based on a legal query.
        Input: A legal query or description of a case.
        Output: A list of relevant BNS sections with their details.
        '''
        # Create the self-querying retriever
        retriever = SelfQueryRetriever.from_llm(
            llm=self.llm,
            vectorstore=self.vectorstore,
            document_contents=self.document_content_description,
            metadata_field_info=self.attribute_info,
            verbose=True  # Set to True to see the generated query
        )

        # Get the relevant documents
        retrieved_docs = retriever.invoke(query)

        # Print the results
        print("Retrieved documents:")
        for doc in retrieved_docs:
            print("-" * 50)
            print("Content:", doc.page_content)
            print("Metadata:", doc.metadata)

        return retrieved_docs