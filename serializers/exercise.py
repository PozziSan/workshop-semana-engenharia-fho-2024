from pydantic import BaseModel


class ExerciseBase(BaseModel):
    name: str
    muscular_group: str | None


class ExerciseCreate(ExerciseBase):
    pass


class Exercise(ExerciseBase):
    id: int

    class Config:
        orm_mode = True
