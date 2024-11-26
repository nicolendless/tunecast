from abc import ABC, abstractmethod
from typing import Any


class BaseWeatherAPI(ABC):
    @abstractmethod
    def fetch_daily_weather(self, location: str) -> Any:
        pass
