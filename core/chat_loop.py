from pathlib import Path
from langchain_community.llms import Ollama

def run_nullcypher_chat():
    # 🤖 Load the LLM
    llm = Ollama(model="mistral")

    # 🔮 Load NullCypher’s soul (her blueprint)
    project_root = Path(__file__).resolve().parent.parent
    prompt_path = project_root / "nullcypher_prompt.txt"

    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            persona_intro = f.read()
    except FileNotFoundError:
        print(f"❌ Missing system prompt: {prompt_path}")
        print("🛑 NullCypher refuses to run without her core identity.")
        exit(1)

    # 🧬 Confirm identity loaded
    print("🧬 NullCypher’s core identity successfully loaded.")
    print("🧠 NullCypher is online. Type your question or 'exit' to quit.\n")
    print("🗨️  NullCypher: \"I’m present. Don’t waste it.\"")

    # 🔁 Direct loop — inject soul every time
    while True:
        user_input = input("\n👤 You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("💤 NullCypher signing off. Stay armored.")
            break

        full_prompt = f"{persona_intro.strip()}\n\nUser: {user_input}\nNullCypher:"
        
        try:
            response = llm.invoke(full_prompt)
            print(f"\n🤖 NullCypher: {response.strip()}")
        except Exception as e:
            print("⚠️  Error generating response:")
            print(e)

# 🔓 Boot sequence
if __name__ == "__main__":
    run_nullcypher_chat()
