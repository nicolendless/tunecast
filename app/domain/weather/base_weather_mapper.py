from abc import ABC, abstractmethod
from app.domain.weather.weather import Weather


class WeatherMapper(ABC):
    @abstractmethod
    def map(self, raw_data: dict) -> Weather:
        pass
