# Law Buddy ⚖️

Law Buddy is an AI-powered legal assistant that helps you with your legal queries. It provides a simple and intuitive interface to search for relevant sections from the Bharatiya Nyaya Sanhita (BNS) and find similar legal cases from the past.

## Features ✨

*   **Legal Section Retrieval:** Get relevant sections from the Bharatiya Nyaya Sanhita (BNS) for your legal queries.
*   **Similar Case Lookup:** Find past legal cases similar to your query, along with their judgments.
*   **Interactive Interface:** A user-friendly web interface built with Streamlit.

## How it Works ⚙️

Law Buddy uses a combination of Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs) to provide accurate and relevant legal information.

1.  **RAG Retriever:** When you enter a query, the RAG retriever searches through a vectorized database of the Bharatiya Nyaya Sanhita (BNS) to find the most relevant sections. This is done using a ChromaDB vector store and HuggingFace sentence transformers for embeddings.

2.  **Case Lookup AI:** The Case Lookup AI uses Google's Generative AI (Gemini) to search the internet for similar legal cases from the past. It returns a structured JSON output with the case name, citation, summary, and judgment.

3.  **Graph-Based Workflow:** The entire process is orchestrated using LangGraph, which manages the flow of information between the RAG retriever and the Case Lookup AI.

## Installation 🚀

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/law-buddy.git
    cd law-buddy
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirement.txt
    ```

4.  **Set up your environment variables:**
    Create a `.env` file in the root directory and add your Gemini API key:
    ```
    GEMINI_API_KEY="your-api-key"
    ```

## Usage ▶️

1.  **Load the legal data into ChromaDB:**
    ```bash
    python lib/RAG/rag_loader.py lib/RAG/bns_sections.csv legal_docs
    ```

2.  **Run the Streamlit application:**
    ```bash
    streamlit run main.py
    ```

3.  Open your browser and go to `http://localhost:8501` to start using Law Buddy.

## Project Structure 📂

```
.
├── main.py                 # Streamlit application
├── requirement.txt        # Project dependencies
├── lib
│   ├── configurations      # Configuration files
│   │   ├── config.yaml
│   │   └── llm_config.yaml
│   ├── core                # Core application logic
│   │   ├── fallback_tool.py
│   │   ├── graph.py
│   │   ├── legal_case_search.py
│   │   ├── legal_helper_tool.py
│   │   ├── ollama.py
│   │   ├── rag_retriever.py
│   │   └── rephraser.py
│   ├── RAG                 # RAG system files
│   │   ├── bns_sections.csv
│   │   └── rag_loader.py
│   └── utils               # Utility functions
│       └── config_reader.py
└── README.md
```

## Contributing 🤝

This project is under active development and we welcome any contributions. Please feel free to open an issue or submit a pull request. More changes are to come, so stay tuned!