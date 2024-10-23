from pydantic import BaseModel

class WorkoutBase(BaseModel):
    name: str
    mesocycle: str
    student_name: str | None = None


class WorkoutCreate(WorkoutBase):
    pass


class Workout(WorkoutBase):
    id: int

    class Config:
        orm_mode = True


class Workouts(BaseModel):
    workouts: list[Workout] = []