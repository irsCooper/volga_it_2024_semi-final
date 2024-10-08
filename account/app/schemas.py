from typing import List
from pydantic import BaseModel


class Role(BaseModel):
    id: int
    nameRole: str
    descriptionRole: str


class User(BaseModel):
    lastName: str
    firstName: str
    fullName: str
    userName: str
    password: str
    roles: List[Role]
