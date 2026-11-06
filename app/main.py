from fastapi import FastAPI, HTTPException

from app.models import ChatRequest, ChatResponse, Message

app = FastAPI(title="AI Engineer 90", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat/echo", response_model=ChatResponse)
def chat_echo(request: ChatRequest) -> ChatResponse:
    """Echo the last user message.

    This is a placeholder: in week 2 the echo is replaced by a real LLM call.
    """
    user_messages = [m for m in request.messages if m.role == "user"]
    if not user_messages:
        raise HTTPException(status_code=422, detail="At least one user message is required")

    text = f"You said: {user_messages[-1].content}"
    return ChatResponse(
        reply=Message(role="assistant", content=text),
        estimated_tokens=max(1, len(text) // 4),
    )
