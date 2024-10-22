from pydantic import BaseModel


class ExerciseBase(BaseModel):
    name: str
    series: str
    repetitions: str


class ExerciseCreate(ExerciseBase):
    pass


class Exercise(ExerciseBase):
    id: int

    class Config:
        orm_mode = True
