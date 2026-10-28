from pydantic import BaseModel,Field
from typing import Literal
class Incident(BaseModel):
    title:str = Field(min_length=5,max_length=150)
    severity:Literal["low","medium","high"]
    status: Literal["open","in_progress","resolved","closed"]
    equipment_id: int=Field(gt=0)