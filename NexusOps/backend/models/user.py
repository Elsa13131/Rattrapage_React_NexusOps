
from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Literal


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    role: Literal["admin", "operator", "viewer"]
