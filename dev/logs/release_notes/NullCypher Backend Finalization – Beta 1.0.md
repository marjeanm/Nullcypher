## 🧠 NullCypher – Backend Architecture

### 🔓 Local Dev Setup

```bash
git clone https://github.com/marjeanm/nullcypher-genai-cyber-assistant.git
cd nullcypher-genai-cyber-assistant
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate (Linux/macOS)
pip install -r requirements.txt
python -m core.chat_loop ```

Requires Python 3.11+, Mistral model running via ollama.

## 📁 Project Structure

| Folder           | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| `core/`          | Main AI runtime: `chat_loop.py`, `persona.py`, `council.py` |
| `logs/footer/`   | Footer logs (daily backend milestones)                      |
| `logs/tests/`    | Persona and council validation logs                         |
| `assistant/`     | Personality templates, tone rules (WIP)                     |
| `scripts/`       | Utility and import tools                                    |
| `memory_chunks/` | Modular memory uploads                                      |

## 🧬 Identity Stack
- persona.py = Core blueprint: tone, behavior, rituals, traits
- council.py = Rogue, Daria, Spectrum logic
- chat_loop.py = Injects prompt, returns live responses from Mistral

## 🛡️ Dev Notes
- Bandit + Pre-commit security checks live
- No dual-tone toggle; logic is trigger-based
- Memory is manually injected (Chroma system WIP)

## ✅ Run a Live Session
python -m core.chat_loop

Expect output
```bash
🧬 NullCypher’s core identity successfully loaded.
🧠 NullCypher is online. Type your question or 'exit' to quit.
🗨️  NullCypher: "I’m present. Don’t waste it."
```

---

## ✅ 2. `core/` Code Review – Docstring Status

| File | Status | Note |
|------|--------|------|
| `chat_loop.py` | ✅ Mostly documented | Suggest: Add 1-line summary atop file |
| `persona.py` | 🟡 No class-level docstring | Recommend: Add `"""Defines NullCypher's persona blueprint."""` to top of class |
| `council.py` | 🟡 No module docstring | Recommend: Add `"Defines internal council roles and triggers."`

## ✅ Suggestion

- Add this to the **top of `council.py`**

```python

"""Defines NullCypher's Inner Council roles, tones, and activation triggers."""
