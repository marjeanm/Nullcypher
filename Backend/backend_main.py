from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import logging

logger = logging.getLogger("nullcypher-chat")
logging.basicConfig(level=logging.INFO)

from assistant.chat_engine import get_streaming_response

app = FastAPI()

# CORES: Allow frontend dev server (vite) to call backend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def generate_response_stream(user_input):
    return get_streaming_response(user_input)


@app.post("/chat")
async def chat_endpoint(request: Request):
    try:
        data = await request.json()
        user_input = data.get("message", "")

        if not isinstance(user_input, str) or len(user_input.strip()) == 0:
            raise HTTPException(status_code=400, detail="Invalid message format.")

        logger.info(f"[INPUT] {user_input.strip()}")

        async def event_stream():
            for token in get_streaming_response(user_input):
                yield token
                await asyncio.sleep(0.05)

        return StreamingResponse(event_stream(), media_type="text/plain")

    except Exception as e:
        logger.error(f"Exception in /chat: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
