from fastapi import FastAPI

from app.container import Container
from app.controllers import weather_controller

app = FastAPI()

container = Container()
container.wire(modules=[weather_controller])

# Include routes
app.include_router(weather_controller.router, prefix="/api/v1", tags=["Weather"])
