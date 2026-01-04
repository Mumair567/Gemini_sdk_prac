from fastapi import FastAPI,APIRouter,HTTPException
from app.chatbot.chat_model import chat_func
from app.schemas.chat_response import ChatResponse
chatbot_router=APIRouter(prefix="/chatbot",tags=["Chatbot"])

@chatbot_router.post("/chat/")
async def chat_bot(user_input:ChatResponse):
    try:
        response=chat_func(user_input.chat_bot_response)
        return {response}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="chatbot service not available"
        )
