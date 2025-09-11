from typing import Sequence
from openai import AsyncOpenAI
from .base import AIProvider, ChatMessage

class OpenAIProvider(AIProvider):
    def __init__(self, api_key: str, model: str) -> None:
        self._client = AsyncOpenAI(api_key=api_key)
        self._model = model

    async def complete(self, messages: Sequence[ChatMessage]) -> str:
        resp = await self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": m["role"], "content": m["content"]} for m in messages],
        )
        return resp.choices[0].message.content or ""
