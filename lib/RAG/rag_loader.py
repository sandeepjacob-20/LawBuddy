from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import pandas as pd
import sys

#function to load csv as documents
def load_csv_as_documents(file_path: str) -> list[Document]:
    df = pd.read_csv(file_path)
    documents = []
    for _, row in df.iterrows():
        data = row.to_dict()
        #creating document with page content as description and metadata as other columns
        documents.append(Document(page_content=data['Description'], 
                                  metadata={
                                    "chapter_number": data["Chapter"],
                                    "chapter_name": data["Chapter_name"],
                                    "chapter_subtype": data["Chapter_subtype"],
                                    "section_number": data["Section"],
                                    "section_name": data["Section _name"],
                                }
                        ))
    return documents

#function to embed documents to chroma db
def embedd_to_chroma(documents: list[Document], collection_name: str):
    #using the huggingface embeddings model
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    
    #creating chroma vector store
    db = Chroma(
    embedding_function=embeddings,
    persist_directory="./chroma_db",
    collection_name=collection_name  # Pass it only once, as a keyword argument
    )
    
    batch_size = 50 # Adjust as needed to stay within rate limits
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]
        print(f"Adding batch {i//batch_size + 1} of size {len(batch)}...")
        
        # Add the current batch of documents to the database
        db.add_documents(batch)
        
    print("Documents embedded and stored in Chroma DB.")
    return

def main():
    if len(sys.argv) < 3:
        print("Usage: python rag_loader.py <csv_file_path> <collection_name>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    collection_name = sys.argv[2]

    #converts the csv into list of Document objects
    documents = load_csv_as_documents(csv_file_path)
    
    #embeds the documents to chroma db
    embedd_to_chroma(documents,collection_name)

    return

if __name__ == "__main__":
    main()