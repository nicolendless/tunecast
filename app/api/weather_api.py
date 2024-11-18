from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Body, Depends, Path, Query, status

from app.api.weather_dto import WeatherDTO
from app.containers import Container
from app.external_apis.visual_crossing_api import VisualCrossingAPI
from app.services.weather_service import WeatherService


router = APIRouter(
    prefix="/weather",
)


@router.get(
    path="",
    name="Get current weather by location",
    response_model=WeatherDTO,
)
@inject
async def get_current_weather(
    location: str,
    weather_service: WeatherService = Depends(Provide[Container.weather_service])
):
    return weather_service.get_current_weather(location)
