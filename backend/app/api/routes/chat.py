# app/api/routes/chat.py
from fastapi import APIRouter, Depends, status, HTTPException, Request
from ...domain.schemas import Message, MessageIn, HistoryOut
from ...services.chat_service import ChatService

router = APIRouter(prefix="/messages", tags=["messages"])

def get_chat_service(request: Request) -> ChatService:
    chat: ChatService | None = getattr(request.app.state, "chat_service", None)
    if chat is None:
        raise HTTPException(status_code=503, detail="ChatService not ready")
    return chat

@router.get("", response_model=HistoryOut)
async def list_messages(chat: ChatService = Depends(get_chat_service)) -> HistoryOut:
    return HistoryOut(items=chat.list())

@router.post("", response_model=Message, status_code=status.HTTP_201_CREATED)
async def send_message(payload: MessageIn, chat: ChatService = Depends(get_chat_service)) -> Message:
    return await chat.post_and_reply(payload)
