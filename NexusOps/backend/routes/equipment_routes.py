
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Literal
from database import SessionLocal
from services.equipment_service import (
    get_all_equipments,
    get_equipment_by_id,
    create_equipment,
    update_equipment,
    delete_equipment
)

router = APIRouter()

class EquipmentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    status: Literal["online", "offline"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/equipments")
def get_equipments(db: Session = Depends(get_db)):
    return get_all_equipments(db)

@router.get("/equipments/{equipment_id}")
def get_equipment(equipment_id: int, db: Session = Depends(get_db)):
    equipment = get_equipment_by_id(db, equipment_id)

    if equipment is None:
        raise HTTPException(status_code=404, detail="Équipement introuvable")

    return equipment

@router.post("/equipments", status_code=201)
def post_equipment(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    return create_equipment(db, equipment.name, equipment.status)