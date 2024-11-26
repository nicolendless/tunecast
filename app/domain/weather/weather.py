from pydantic import BaseModel


class Weather(BaseModel):
    temperature: float
    humidity: float
    precipitation_probability: float
    snow_inches: float
    wind_speed: float
    cloud_cover: float
    visibility: float
    uv_index: float


# {
#     'datetime': '2024-11-19',
#     'datetimeEpoch': 1731970800,
#     'tempmax': 19.2,
#     'tempmin': 9.5,
#     'temp': 14.7,
#     'feelslikemax': 19.2,
#     'feelslikemin': 7.8,
#     'feelslike': 14.4,
#     'dew': 10.9,
#     'humidity': 78.5,
#     'precip': 0.0,
#     'precipprob': 0.0,
#     'precipcover': 0.0,
#     'preciptype': None,
#     'snow': 0.0,
#     'snowdepth': 0.0,
#     'windgust': 40.7,
#     'windspeed': 15.5,
#     'winddir': 268.7,
#     'pressure': 1015.3,
#     'cloudcover': 23.8,
#     'visibility': 16.4,
#     'solarradiation': 107.4,
#     'solarenergy': 9.3,
#     'uvindex': 5.0,
#     'severerisk': 10.0,
#     'sunrise': '07:44:59',
#     'sunriseEpoch': 1731998699,
#     'sunset': '17:28:19',
#     'sunsetEpoch': 1732033699,
#     'moonphase': 0.62,
#     'conditions': 'Partially cloudy',
#     'description': 'Partly cloudy throughout the day.',
#     'icon': 'partly-cloudy-day',
#     'stations': ['LEBL', 'D1298', 'LEGE', 'LELL'],
#     'source': 'comb'
# }

