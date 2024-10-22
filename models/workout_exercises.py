from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.base import BaseModel

class WorkoutExerciseModel(BaseModel):
    __tablename__ = "workout_exercises"

    workout_id = Column(Integer, ForeignKey("workouts.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)
    series = Column(Integer, nullable=False)
    repetitions = Column(Integer, nullable=False)
    instructions = Column(String, nullable=True)

    workout = relationship("WorkoutModel", back_populates="workout_exercises", uselist=False)
    exercises = relationship("ExerciseModel", back_populates="workout_exercises")