from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(
    prefix="/Docktors",
    tags=["Docktors"]
)


@router.get("/")
async def get_all_doctors():
    pass


@router.get("/{id}")
async def get_docktor_by_id(id: Annotated[int, Path(ge=1)]):
    pass