from typing import Literal

from pydantic import BaseModel, Field


class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str = Field(min_length=1, max_length=4000)


class ChatRequest(BaseModel):
    messages: list[Message] = Field(min_length=1)


class ChatResponse(BaseModel):
    reply: Message
    # Rough estimate (about 4 characters per token). Week 2 replaces this
    # with the real token counts returned by the LLM API.
    estimated_tokens: int
