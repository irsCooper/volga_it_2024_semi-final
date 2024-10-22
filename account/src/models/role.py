from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

class Role(Base):
    __tablename__ = 'roles'
    
    nameRole: Mapped[str] = mapped_column(nullable=False)