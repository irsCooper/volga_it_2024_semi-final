from typing import Annotated
from fastapi import APIRouter, Path

router = APIRouter(
    prefix="/Accounts",
    tags=["Accounts"]
)


@router.get("/Me")
async def me():
    pass


@router.put("/Update")
async def update():
    pass


@router.get("/")
async def accounts():
    pass


@router.post("/")
async def set_new_account():
    pass


@router.put("/{id}")
async def update_account_by_id(id: Annotated[int, Path(ge=1)]):
    pass


@router.delete("/{id}")
async def delete_account_by_id(id: Annotated[int, Path(ge=1)]):
    pass