from fastapi import FastAPI

from controllers import health, workout
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(health.router)
app.include_router(workout.router)