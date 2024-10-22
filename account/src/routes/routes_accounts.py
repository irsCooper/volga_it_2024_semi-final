from typing import Annotated
from fastapi import APIRouter, Path

from schemas.schemas import User, UserBase
from api import user_crud as crud

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


@router.get("/", response_model=list[User])
async def accounts(session):
    return await crud.get_users(session=session)


@router.post("/")
async def set_new_account():
    pass


@router.put("/{id}")
async def update_account_by_id(id: Annotated[int, Path(ge=1)]):
    pass


@router.delete("/{id}")
async def delete_account_by_id(id: Annotated[int, Path(ge=1)]):
    pass