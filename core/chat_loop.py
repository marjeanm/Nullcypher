from langchain_ollama import OllamaLLM
from core.persona import NullCypherPersona


def run_nullcypher_chat():
    # 🤖 Load the LLM
    llm = OllamaLLM(model="mistral")

    # 🧠 Load NullCypher’s personality and tone
    persona = NullCypherPersona()

    # 🧠 DEBUG: Confirm persona object has the council attribute
    print("DEBUG: Persona loaded. Has council?", hasattr(persona, "inner_council"))

    # 🧬 Inject identity and council summary
    council_intro = persona.get_council_summary()
    base_prompt = f"{persona.speak_identity()}\n\n🧠 Council Roster:\n{council_intro}"

    # ✅ Confirm council
    print("💡 Council Summary:\n")
    print(council_intro)

    print("\n🧠 NullCypher is online. Type your question or 'exit' to quit.")
    print('🗨️  NullCypher: "I’m here,I move with intention even when I’m quiet."')

    # 🔁 Live prompt-response loop
    while True:
        user_input = input("\n👤 You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("💤 NullCypher signing off. Stay armored.")
            break

        full_prompt = f"{base_prompt.strip()}\n\nUser: {user_input}\nNullCypher:"
        try:
            response = llm.invoke(full_prompt)
            print(f"\n🤖 NullCypher: {response.strip()}")
        except Exception as e:
            print("⚠️  Error generating response:")
            print(e)


# 🔓 Entry point
if __name__ == "__main__":
    run_nullcypher_chat()
