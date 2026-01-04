import os
import requests
from fastapi import FastAPI, APIRouter,HTTPException

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("Weather_API_KEY")
BASE_URL = os.getenv("WEATHERAPI_BASE_URL")

weather_router=APIRouter(prefix="/weather_info",tags=["Weather_info"])

@weather_router.get("/weather/{city_weather}")
async def weather_city(city:str):
    try:
        if not API_KEY:
            raise HTTPException(status_code=404,detail="API key Not found")
        response = requests.get(
            f"{BASE_URL}/current.json",
            params={"key": API_KEY, "q": city}
        )
        data=response.json()
        return data
    except Exception:
        raise HTTPException(status_code=500,detail="Internal server error cannot process your request")
