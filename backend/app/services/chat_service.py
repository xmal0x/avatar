from collections import deque
from datetime import datetime
from threading import Lock
from typing import List

from ..domain.schemas import Message, MessageIn
from ..adapters.ai.base import AIProvider, ChatMessage

class ChatService:
    def __init__(self, ai: AIProvider, system_prompt: str, max_messages: int = 200) -> None:
        self._ai = ai
        self._system_prompt = system_prompt
        self._messages: deque[Message] = deque(maxlen=max_messages)
        self._lock = Lock()
        self._next_id = 1

    def list(self) -> List[Message]:
        with self._lock:
            return list(self._messages)

    async def post_and_reply(self, payload: MessageIn) -> Message:
        with self._lock:
            user = Message(
                id=self._next_id, role="user",
                content=payload.content.strip(), created_at=datetime.utcnow()
            )
            self._next_id += 1
            self._messages.append(user)
            history_dict: list[ChatMessage] = [{"role":"system","content": self._system_prompt}]
            history_dict += [m.model_dump() for m in self._messages] 

        ai_text = await self._ai.complete(history_dict)

        with self._lock:
            ai = Message(
                id=self._next_id, role="assistant",
                content=ai_text, created_at=datetime.utcnow()
            )
            self._next_id += 1
            self._messages.append(ai)
            return ai
