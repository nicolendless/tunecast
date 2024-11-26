from dependency_injector import containers, providers

from app.external_apis.spotify_api import SpotifyAPI
from app.external_apis.spotify_api_settings import SpotifyAPISettings
from app.external_apis.visual_crossing_api import VisualCrossingAPI
from app.external_apis.visual_crossing_api_settings import VisualCrossingAPISettings
from app.services.genre_mapping_service import GenreMappingService
from app.services.suggestion_service import SuggestionService
from app.services.weather_service import WeatherService


class Container(containers.DeclarativeContainer):

    visual_crossing_api_settings = providers.Singleton(VisualCrossingAPISettings)
    spotify_api_settings = providers.Singleton(SpotifyAPISettings)

    visual_crossing_api = providers.Singleton(
        VisualCrossingAPI,
        api_key=visual_crossing_api_settings().api_key,
    )

    spotify_api = providers.Singleton(
        SpotifyAPI,
        client_id=spotify_api_settings().client_id,
        client_secret=spotify_api_settings().client_secret
    )

    weather_service = providers.Singleton(
        WeatherService,
        external_weather_api=visual_crossing_api,
    )

    genre_mapping_service = providers.Singleton(
        GenreMappingService,
    )

    suggestion_service = providers.Singleton(
        SuggestionService,
        weather_service=weather_service,
        spotify_api=spotify_api,
        genre_mapping_service=genre_mapping_service,
    )


