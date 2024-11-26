from dependency_injector import containers, providers

from app.application.mappers.visual_crossing_api_mapper import VisualCrossingAPIMapper
from app.infrastructure.visual_crossing_api import VisualCrossingAPI
from app.infrastructure.visual_crossing_api_settings import VisualCrossingAPISettings
from app.application.services.weather_service import WeatherService


class Container(containers.DeclarativeContainer):

    visual_crossing_api_settings = providers.Singleton(VisualCrossingAPISettings)
    visual_crossing_api = providers.Singleton(
        VisualCrossingAPI,
        api_key=visual_crossing_api_settings().api_key,
    )

    visual_crossing_api_mapper = providers.Singleton(VisualCrossingAPIMapper)
    weather_service = providers.Singleton(
        WeatherService,
        external_weather_api=visual_crossing_api,
        weather_mapper=visual_crossing_api_mapper,
    )


