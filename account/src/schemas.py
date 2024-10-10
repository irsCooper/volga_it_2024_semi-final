from typing import List
from pydantic import BaseModel, Field


class Role(BaseModel):
    nameRole: str


class User(BaseModel):
    lastName: str 
    firstName: str 
    fullName: str 
    userName: str 
    password: str = Field(min_length=8)
    roles: List[Role]
