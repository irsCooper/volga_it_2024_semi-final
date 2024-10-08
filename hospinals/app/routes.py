from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(
    prefix="/Hospitals",
    tags=["Hospitals"]
)


@router.get("/")
async def get_all_hospitals():
    pass


@router.get("/{id}")
async def get_hospital_by_id(id: Annotated[int, Path(ge=1)]):
    pass

@router.get("/{id}/Rooms")
async def get_rooms_in_hospital_by_id(id: Annotated[int, Path(ge=1)]):
    pass


@router.post("/")
async def set_hospital():
    pass



@router.put("/{id}")
async def update_hospital_by_id(id: Annotated[int, Path(ge=1)]):
    pass

@router.delete("/{id}")
async def delete_hospital_by_id(id: Annotated[int, Path(ge=1)]):
    pass