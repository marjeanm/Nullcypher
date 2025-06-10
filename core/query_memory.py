import os
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_memory_response(query: str, k: int = 3) -> str:
    base_dir = os.path.dirname(__file__)
    memory_dir = os.path.abspath(os.path.join(base_dir, '..', 'nullcypher_memory_store'))

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory=memory_dir, embedding_function=embedding_model)

    docs = vectorstore.similarity_search(query, k=k)
    
    if not docs:
        return "I couldn't find anything in memory for that. You wanna teach me something new?"

    return "\n\n".join([doc.page_content for doc in docs])
