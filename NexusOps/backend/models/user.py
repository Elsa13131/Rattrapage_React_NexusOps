from pydantic import BaseModel,Field,EmailStr
from typing import Literal
class User(BaseModel):
    id:int
    name:str = Field(min_length=2,max_length=100)
    email:EmailStr
    role:Literal["admin","operator","viewer"]