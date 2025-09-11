from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field

Role = Literal["user", "assistant"]

class Message(BaseModel):
    id: int
    role: Role
    content: str
    created_at: datetime

class MessageIn(BaseModel):
    content: str = Field(min_length=1, max_length=4000)

class HistoryOut(BaseModel):
    items: list[Message]