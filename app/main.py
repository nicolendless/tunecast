from fastapi import FastAPI
from app.api import weather_api
from app.containers import Container

app = FastAPI()

container = Container()
container.wire(modules=[weather_api])

# Include routes
app.include_router(weather_api.router, prefix="/api/v1", tags=["Weather"])
