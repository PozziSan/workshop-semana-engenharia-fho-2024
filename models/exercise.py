from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base import BaseModel


class ExerciseModel(BaseModel):
    __tablename__ = "exercises"

    name = Column(String, nullable=False)
    muscular_group = Column(String, nullable=True)

    workout_exercises = relationship("WorkoutExerciseModel", back_populates="exercise")
