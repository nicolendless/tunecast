from app.domain.weather.base_weather_mapper import BaseWeatherMapper
from app.domain.weather.weather import Weather


class VisualCrossingAPIMapper(BaseWeatherMapper):
    def map(self, raw_data: dict) -> Weather:
        if not raw_data or "days" not in raw_data:
            raise ValueError("Invalid response structure from the VisualCrossing API.")

        weather = raw_data["days"][0]

        return Weather(
            temperature=weather.get("feelslike"),
            humidity=weather.get("humidity"),
            precipitation_probability=weather.get("precipprob"),
            snow_inches=weather.get("snow"),
            wind_speed=weather.get("windspeed"),
            cloud_cover=weather.get("cloudcover"),
            visibility=weather.get("visibility"),
            uv_index=weather.get("uvindex")
        )
