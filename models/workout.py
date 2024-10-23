from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base import BaseModel

class WorkoutModel(BaseModel):
    __tablename__ = "workouts"
    
    name = Column(String, nullable=False)
    mesocycle = Column(String, nullable=False)
    student_name = Column(String, nullable=True)

    workout_exercises = relationship("WorkoutExerciseModel", back_populates="workout")