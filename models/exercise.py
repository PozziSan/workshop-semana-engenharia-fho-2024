from sqlalchemy import Column, String, Integer

from models.base import BaseModel


class ExerciseModel(BaseModel):
    __tablename__ = "exercises"

    name = Column(String, nullable=False)
    series = Column(Integer, nullable=False)
    repetitions = Column(Integer, nullable=False)
