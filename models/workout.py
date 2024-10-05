from sqlalchemy import Column, String, Integer

from models.base import BaseModel

class WorkoutModel(BaseModel):
    __tablename__ = "workouts"
    
    name = Column(String, nullable=False)
    mesocycle = Column(String, nullable=False)
    studant_name = Column(String, nullable=True)