from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException

from app.container import Container
from app.application.use_cases.weather_use_case import WeatherUseCase
from app.domain.weather.weather import Weather

router = APIRouter(
    prefix="/weather",
)


@router.get(
    path="",
    name="Get current daily weather by location",
    response_model=Weather,
)
@inject
async def get_current_weather(
    location: str,
    weather_use_case: WeatherUseCase = Depends(Provide[Container.weather_use_case])
):
    try:
        return weather_use_case.get_daily_weather(location)
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error fetching weather data: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"An unexpected error occurred: {str(e)}"
        )

