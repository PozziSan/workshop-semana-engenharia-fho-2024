from pydantic import BaseModel

from serializers.exercise import Exercise
from serializers.workout import Workout


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

    workout: Workout
    exercise: Exercise


class WorkoutExercises(BaseModel):
    workout_exercises: list[WorkoutExercise] = []
