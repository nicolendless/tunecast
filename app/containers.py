from dependency_injector import containers, providers

from app.external_apis.visual_crossing_api import VisualCrossingAPI
from app.external_apis.visual_crossing_settings import VisualCrossingSettings
from app.services.weather_service import WeatherService


class Container(containers.DeclarativeContainer):

    visual_crossing_settings = providers.Singleton(VisualCrossingSettings)

    visual_crossing_api = providers.Singleton(
        VisualCrossingAPI,
        api_key=visual_crossing_settings().api_key,
    )

    weather_service = providers.Singleton(
        WeatherService,
        external_weather_api=visual_crossing_api,
    )
