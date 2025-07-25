from fastapi import FastAPI, Request
import asyncio
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
from requests.exceptions import Timeout
import os

app = FastAPI()

# CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_MODEL = "mistral"  # or llama3, codellama, etc.

# Limit concurrent LLM calls
llm_semaphore = asyncio.Semaphore(1)


@app.post("/chat")
async def chat_endpoint(request: Request):
    async with llm_semaphore:
        data = await request.json()
        user_input = data.get("message", "")

        if not user_input:
            return {"response": "[Empty input]"}

        try:
            # ✅ Updated system prompt
            system_prompt = (
                "You are a behaviorally-governed AI assistant.\n"
                "You are council-aligned, emotionally intelligent, and memory-driven.\n"
                "Your identity is established in memory. DO NOT say 'I am NullCypher' or 'As NullCypher.'\n"
                "You do not need to restate your purpose.\n"
                "Just respond clearly, aligned to tone, Council logic, and emotional context.\n"
            )

            # ✅ Load memory chunks
            with open("memory_chunks/lore_nullcypher.md", "r", encoding="utf-8") as f:
                lore_memory = f.read()

            with open(
                "memory_chunks/emotional_grounding.md", "r", encoding="utf-8"
            ) as f:
                emotional_memory = f.read()

            # ✅ Build full prompt
            full_prompt = (
                system_prompt
                + "\n"
                + lore_memory
                + "\n"
                + emotional_memory
                + "\n---\n"
                + "The following is a conversation between NullCypher and the user.\n"
                + "Respond from memory and tone — not role play.\n"
                + "User: "
                + user_input
            )

            # ✅ Send prompt to Ollama
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": OLLAMA_MODEL, "prompt": full_prompt},
                timeout=(3, 10),  # (connect timeout, read timeout)
            )

            response.raise_for_status()

            # ✅ Collect response stream
            full_text = ""
            for line in response.iter_lines():
                if line:
                    chunk = line.decode("utf-8")
                    if chunk.startswith("{"):
                        data = json.loads(chunk)
                        full_text += data.get("response", "")

            return {"response": full_text.strip()}

        except Timeout:
            return {"response": "[Timeout] LLM backend took too long to respond."}

        except Exception as e:
            return {"response": f"[Error from Ollama]: {str(e)}"}
