# 🧠 NullCypher – Generative AI Assistant (Backend)

## 🚀 Project Boot Instructions

Clone the repo and run NullCypher locally in development mode:

```git clone https://github.com/marjeanm/nullcypher-genai-cyber-assistant.git
cd nullcypher-genai-cyber-assistant
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
python -m core.chat_loop
```

Requires: Python 3.11+, ollama running locally, Mistral model installed.

| Folder           | Purpose                                                         |
| ---------------- | --------------------------------------------------------------- |
| `core/`          | Main chatbot logic (`chat_loop.py`, `persona.py`, `council.py`) |
| `logs/`          | Daily footer logs and test sessions                             |
| `memory_chunks/` | Static vector memory files                                      |
| `scripts/`       | Optional tools and utilities                                    |
| `src/`           | (Legacy logic or future experimental modules)                   |
| `assistant/`     | Persona templates, tone models, ritual logic (WIP)              |

💬  Persona Engine
persona.py: Defines NullCypher’s identity, tone, and inner council
council.py: Logic for council behavior triggers and voice summaries
chat_loop.py: Main runtime loop, handles prompt injection + model output

## 🔐 Developer Notes
Bandit security checks (pre-commit enforced)
Footer logs stored under logs/footer/YYYY-MM-DD-footer.md
Test logs go under logs/tests/
All persona logic tied to council activation triggers (no toggles)

## 📦 Backend Status: Beta-Ready

- ✔️ Prompt chaining stable

- ✔️ Council logic firing properly

- ✔️ Memory system (manual load) in place
- ✔️ Git structure locked
- ❌ Frontend not yet implemented

## 🧠 To Run a Local Session

```python -m core.chat_loop```

Expect to see:

```markdown
🧬 NullCypher’s core identity successfully loaded.
🧠 NullCypher is online. Type your question or 'exit' to quit.
🗨️  NullCypher: "I’m present. Don’t waste it."
```
