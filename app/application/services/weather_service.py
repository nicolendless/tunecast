from app.domain.weather.base_weather_mapper import BaseWeatherMapper
from app.domain.weather.weather import Weather
from app.domain.weather.base_weather_api import BaseWeatherAPI


class WeatherUseCase:
    def __init__(self, external_weather_api: BaseWeatherAPI, weather_mapper: BaseWeatherMapper):
        self.external_weather_api = external_weather_api
        self.weather_mapper = weather_mapper

    def get_daily_weather(self, location: str) -> Weather:
        response = self._fetch_weather_data(location)
        return self.weather_mapper.map(response)

    def _fetch_weather_data(self, location: str) -> dict:
        try:
            response = self.external_weather_api.fetch_daily_weather(location)
            if not response:
                raise ValueError("Empty response from external weather API.")
            return response
        except Exception as e:
            raise ValueError(f"Failed to fetch weather data: {str(e)}")

