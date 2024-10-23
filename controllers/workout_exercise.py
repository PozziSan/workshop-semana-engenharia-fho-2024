from fastapi import APIRouter
from fastapi.responses import JSONResponse

from exceptions import NotFoundException
from models.workout_exercises import WorkoutExerciseModel
from serializers.workout_exercise import (
    WorkoutExercise,
    WorkoutExercises,
    WorkoutExerciseCreate,
)

router = APIRouter(prefix="/workout/exercises", tags=["Workout"])


@router.get("/", response_model=WorkoutExercises)
def get_all():
    workout_exercises = WorkoutExerciseModel.all()

    return {"workout_exercises": workout_exercises}


@router.post("/", response_model=WorkoutExercise)
def create(workout_exercise: WorkoutExerciseCreate):
    return WorkoutExerciseModel.create(**workout_exercise.model_dump())


@router.delete("/{workout_exercise_id}")
def delete(workout_exercise_id: int):
    workout_exercise = WorkoutExerciseModel.get_by_id(workout_exercise_id)

    if not workout_exercise:
        raise NotFoundException()

    workout_exercise.delete()

    return JSONResponse(status_code=200, content={"message": "Success"})


@router.get("/{workout_id}", response_model=WorkoutExercises)
def get_by_workout_id(workout_id: int):
    workout_exercises = WorkoutExerciseModel.get_all_by(workout_id=workout_id)

    print(workout_exercises)

    return {"workout_exercises": workout_exercises}
