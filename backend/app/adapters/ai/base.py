from abc import ABC, abstractmethod
from typing import Sequence, TypedDict, Literal

Role = Literal["system", "user", "assistant"]

class ChatMessage(TypedDict):
    role: Role
    content: str

class AIProvider(ABC):
    @abstractmethod
    async def complete(self, messages: Sequence[ChatMessage]) -> str:
        """Return the text of the assistant's response to the history."""
        raise NotImplementedError
