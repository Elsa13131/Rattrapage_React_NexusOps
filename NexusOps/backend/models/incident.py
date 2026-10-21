from pydantic import BaseModel

class Incident(BaseModel):
    title:str
    severity:str
    status:str
    equipment_id:int