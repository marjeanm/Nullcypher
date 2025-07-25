from pathlib import Path
from langchain_community.llms import Ollama

# Load prompt at startup
project_root = Path(__file__).resolve().parent.parent
prompt_path = project_root / "nullcypher_prompt.txt"

try:
    with open(prompt_path, "r", encoding="utf-8") as f:
        persona_intro = f.read()
except FileNotFoundError:
    raise RuntimeError(f"❌ Missing system prompt: {prompt_path}")

# Initialize the LLM
llm = Ollama(model="mistral")


# Streaming response for FastAPI
def get_streaming_response(user_input: str):
    full_prompt = f"{persona_intro.strip()}\n\nUser: {user_input}\nNullCypher:"

    try:
        response = llm.invoke(full_prompt)
        for token in response.strip().split():
            yield token + " "
    except Exception as e:
        yield "⚠️ Error: NullCypher encountered a failure.\n"
        yield f"Details: {str(e)}"
