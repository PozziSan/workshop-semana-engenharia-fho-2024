from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from controllers import health, exercise, workout, workout_exercise
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(health.router)
app.include_router(workout.router)
app.include_router(exercise.router)
app.include_router(workout_exercise.router)


@app.exception_handler(Exception)
def generic_exception_handler(req: Request, exception: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )
