
from pydantic import BaseModel, EmailStr, Field
from typing import Literal


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    role: Literal["admin", "operator", "viewer"]
    password: str = Field(min_length=8, max_length=128)
