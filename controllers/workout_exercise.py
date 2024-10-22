from fastapi import FastAPI, APIRouter

from models.workout_exercises import WorkoutExerciseModel
from serializers.workout_exercise import WorkoutExercise, WorkoutExercises, WorkoutExerciseCreate

router = APIRouter(prefix="/workout/exercises", tags=["Workout"])

@router.get("/", response_model=WorkoutExercises)
def get_all():
    workout_exercises = WorkoutExerciseModel.all()

    return {"workout_exercises": workout_exercises}


@router.post("/", response_model=WorkoutExercise)
def create(workout_exercise: WorkoutExerciseCreate):
    return WorkoutExerciseModel.create(**workout_exercise.model_dump())
