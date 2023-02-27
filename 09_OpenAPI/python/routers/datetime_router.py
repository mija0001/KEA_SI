from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/datetime", tags=["datetime"], response_model=datetime)
def get_datetime():
    return datetime.now()