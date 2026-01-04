from fastapi import FastAPI,APIRouter
from app.routers.auth_router import auth_router
from app.routers.chatbot_router import chatbot_router
from app.routers.weather_router import weather_router
app=FastAPI()
app.include_router(auth_router)
app.include_router(chatbot_router)
app.include_router(weather_router)
