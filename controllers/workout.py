from fastapi import APIRouter
from fastapi.responses import JSONResponse

from exceptions import NotFoundException
from serializers.workout import Workout, WorkoutCreate
from models.workout import WorkoutModel


router = APIRouter(prefix="/workout", tags=["Workout"])

@router.get("/", response_model=Workout)
def get_all() -> list[WorkoutModel]:
    return WorkoutModel.all()

@router.post("/", response_model=Workout)
def create(workout: WorkoutCreate) -> WorkoutModel:
    return WorkoutModel.create(**workout.model_dump())

@router.delete("/{workout_id}")
def delete(workout_id: int):
    workout = WorkoutModel.get_by_id(workout_id)

    if not workout:
        raise NotFoundException()
    
    workout.delete()

    return JSONResponse(status_code=200, content={"message": "Success"})
