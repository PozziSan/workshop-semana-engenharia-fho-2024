from fastapi import APIRouter
from fastapi.responses import JSONResponse

from exceptions import NotFoundException
from serializers.exercise import Exercise, ExerciseCreate
from models.exercise import ExerciseModel

router = APIRouter(prefix="/exercise", tags=["Exercise"])


@router.get("/", response_model=Exercise)
def get_all():
    exercises = ExerciseModel.all()
    
    return {"exercises": exercises}


@router.post("/", response_model=Exercise)
def create(exercise: ExerciseCreate) -> ExerciseCreate:
    return ExerciseModel.create(**exercise.model_dump())


@router.delete("/{exercise_id}")
def delete(exercise_id: int):
    exercise = ExerciseModel.get_by_id(exercise_id)

    if not exercise:
        raise NotFoundException()

    return JSONResponse(status_code=200, content={"message": "Success"})
