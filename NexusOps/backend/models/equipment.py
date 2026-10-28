from pydantic import BaseModel,Field
from typing import Literal
class Equipment (BaseModel):
    id:int
    name:str = Field(min_length=2,max_length=100)
    status: Literal["online","offline"]