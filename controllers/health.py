from fastapi import APIRouter
from database import is_database_up

router = APIRouter()

@router.get("/__health", tags=["health"])
def health():
    is_healthy = is_database_up()

    return {"is_healthy": is_healthy, "status": 200}
