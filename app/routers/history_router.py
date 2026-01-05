from fastapi import FastAPI,APIRouter,HTTPException
from app.chatbot.chat_model import history
history_router=APIRouter(prefix="/history",tags=["History"])

@history_router.get("/show_history")

def show():
    try:
        return {"history":history}
    except Exception:
        HTTPException(status_code=404,detail="History not available ")

@history_router.get("/clear_history")

def clear():
    try:
        return {"Empty history":history.clear()}
    
    except Exception:
        HTTPException(status_code=500,detail="Internal server error")