from fastapi import APIRouter

from serializers.workout import Workout, WorkoutCreate
from models.workout import WorkoutModel


router = APIRouter(prefix="/workout", tags=["Workout"])

@router.get("/", response_model=Workout)
def get_all() -> list[WorkoutModel]:
    return WorkoutModel.all()

@router.post("/", response_model=Workout)
def create(train: WorkoutCreate) -> WorkoutModel:
    return WorkoutModel.create(**train.model_dump())

@router.delete("/{train_id}")
def delete(train_id: int):
    train = WorkoutModel.get_by_id(train_id)

    if not train:
        return {"status": 404}
    
    train.delete()

    return {"status": 200}