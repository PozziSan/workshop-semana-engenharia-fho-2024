from fastapi import FastAPI
from fastapi.responses import JSONResponse

from controllers import health, workout
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(health.router)
app.include_router(workout.router)

@app.exception_handler(Exception)
def generic_exception_handler():
    return JSONResponse(
        status_code=418,
        content={"message": "Internal Server Error"},
    )