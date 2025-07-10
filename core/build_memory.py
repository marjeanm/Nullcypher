from pathlib import Path
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Set root directory of the project
project_root = Path(__file__).resolve().parent.parent
memory_dir = project_root / "memory_chunks"

# Read prompt and traits (core memory)
with open(project_root / "nullcypher_prompt.txt", "r", encoding="utf-8") as f:
    prompt_text = f.read()

with open(project_root / "data" / "nullcypher_traits.md", "r", encoding="utf-8") as f:
    trait_text = f.read()

# Gather all .md files in memory_chunks/
memory_files = list(memory_dir.glob("*.md"))

# Read all memory chunk files into one string
memory_texts = []
for file in memory_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        memory_texts.append(content)

# Combine everything into full memory
full_memory = prompt_text + "\n\n" + trait_text + "\n\n" + "\n\n".join(memory_texts)

# Chunk it
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(full_memory)

# Embed & persist
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = Chroma.from_texts(
    chunks,
    embedding_model,
    persist_directory=str(project_root / "nullcypher_memory_store"),
)
vectorstore.persist()

print(
    f"✅ Memory embedded: {len(chunks)} chunks stored from {len(memory_files)} memory files."
)
