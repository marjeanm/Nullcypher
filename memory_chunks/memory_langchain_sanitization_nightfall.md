# LangChain Prompt Injection Sanitization – Nightfall AI

**Source:** [link [source]]( https://help.nightfall.ai/nightfall-firewall-for-ai/tutorials)

genai-protection/langchain-prompt-sanitization-tutorial  

**Tags:** langchain, genai_security, prompt_injection, input_sanitization, nightfall_ai

---

LangChain applications are vulnerable to prompt injection attacks, especially when untrusted user input is passed directly into prompts without sanitization. Nightfall AI demonstrates how to use their GenAI Firewall to scan user inputs and block malicious content before it reaches the language model.

**Key takeaways:**

- Use allowlists, blocklists, or regex filters to

screen inputs  

- Sanitize prompts dynamically to reduce injection

vectors

- Combine semantic scanning with business context

filters for stronger protection  

- LangChain’s flexibility means you must build your

own guardrails unless using a managed tool like Nightfall AI’s SDK

Security is not just about restricting what users say — it's about controlling what gets injected into the model's reasoning context.

---

## NullCypher Use Example

“Looks like you're building a LangChain input handler. Want me to apply sanitization like in the Nightfall AI example?”
