from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()

class Spacecraft(BaseModel):
    id: int
    name: str

    
spacecrafts = [
    {"id": 1, "name": "Voyager 1"},
    {"id": 2, "name": "Voyager 2"},
    {"id": 3, "name": "Cassini"},
    {"id": 4, "name": "Pioneer 10"},
    {"id": 5, "name": "Pioneer 11"},
    {"id": 6, "name": "New Horizons"}
]


@router.get("/spacecrafts/{spacecraft_id}", tags=["spacecrafts"], response_model=Spacecraft)
def get_spacecraft(spacecraft_id: int, show_id: str | None = Query("Default", min_length=2, max_length=50)):
    for spacecraft in spacecrafts:
        if spacecraft["id"] == spacecraft_id:
            if show_id != "Default":
                return {"name": spacecraft["name"]}
            return spacecraft


@router.post("/spacecrafts", tags=["spacecrafts"], response_model=Spacecraft)
def add_spacecraft(spacecraft: Spacecraft):
    spacecrafts.append(spacecraft)
    return spacecraft