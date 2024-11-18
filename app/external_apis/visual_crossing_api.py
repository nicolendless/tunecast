import requests


class VisualCrossingAPI:
    def __init__(self, api_key: str):
        self.base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        self.api_key = api_key

    def get_weather(self, location: str):
        params = {
            "unitGroup": "metric",
            "include": "current",
            "key": self.api_key,
            "contentType": "json"
        }

        url = f"{self.base_url}/{location}"
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
