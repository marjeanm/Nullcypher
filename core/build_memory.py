from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Load core memory sources
with open("nullcypher_prompt.txt", "r", encoding="utf-8") as f:
    system_text = f.read()

with open("NullCypher_TraitCards_FULL.md", "r", encoding="utf-8") as f:
    trait_text = f.read()

full_memory = system_text + "\n\n" + trait_text

# Split memory into chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(full_memory)

# Embed and persist to Chroma
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_texts(chunks, embedding_model, persist_directory="nullcypher_memory_store")
vectorstore.persist()

print(f"✅ Memory embedded: {len(chunks)} chunks stored.")
