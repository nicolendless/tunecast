from app.api.weather_dto import WeatherDTO
from app.external_apis.visual_crossing_api import VisualCrossingAPI


class WeatherService:
    def __init__(self, external_weather_api: VisualCrossingAPI):
        self.external_weather_api = external_weather_api

    def get_current_weather(self, location: str):
        response = self.external_weather_api.get_weather(location)
        current_weather = response["currentConditions"]
        return WeatherDTO(
            conditions=current_weather["conditions"],
            temperature=current_weather["feelslike"]
        )

