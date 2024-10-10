from typing import Annotated
from fastapi import APIRouter, HTTPException, Path
from pydantic import ValidationError

from src.schemas import Role, User

router = APIRouter(
    prefix="/Authentication",
    tags=["Authentication"]
)


@router.post("/SignUp")
async def sign_up(lastName:str, firstName:str, userName:str, password:str):
    try:
        user = User(
            lastName=lastName, 
            firstName=firstName, 
            fullName=firstName + " " + lastName, 
            userName=userName, 
            password=password, 
            roles=[Role(nameRole="user")]
        )
        return {
            "user": user
        }
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())


@router.post("/SignIn")
async def sign_in():
    pass


@router.put("/SignOut")
async def sign_out():
    pass


@router.get("/Validate")
async def validate():
    pass


@router.post("/Refresh")
async def refresh():
    pass