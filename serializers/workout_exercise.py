from pydantic import BaseModel

from serializers.exercise import Exercises

class WorkoutExerciseBase(BaseModel):
    workout_id: int
    exercise_id: int
    series: int
    repetitions: int
    instructions: str | None = None


class WorkoutExerciseCreate(WorkoutExerciseBase):
    pass


class WorkoutExercise(WorkoutExerciseBase):
    id: int


class WorkoutExercises(BaseModel):
    workout_exercises: list[WorkoutExercise] = []
