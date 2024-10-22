from typing import List
from pydantic import BaseModel, ConfigDict, Field


class Role(BaseModel):
    id: int
    nameRole: str


class UserBase(BaseModel):
    id: int
    lastName: str 
    firstName: str 
    fullName: str 
    userName: str 
    password: str = Field(min_length=8)
    roles: List[Role]


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class UserRole(BaseModel):
    id: int
    user_id: int
    role_id: int