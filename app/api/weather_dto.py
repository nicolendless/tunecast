from pydantic import BaseModel


class WeatherDTO(BaseModel):
    conditions: str
    temperature: float
