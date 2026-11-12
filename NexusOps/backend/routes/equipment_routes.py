
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Literal

from database import get_db
from services.auth_dependencies import get_current_user, require_roles
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


@router.get("/equipments")
def get_equipments(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_all_equipments(db)


@router.get("/equipments/{equipment_id}")
def get_equipment(
    equipment_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    equipment = get_equipment_by_id(db, equipment_id)

    if equipment is None:
        raise HTTPException(
            status_code=404,
            detail="Équipement introuvable"
        )

    return equipment


@router.post("/equipments", status_code=201)
def post_equipment(
    equipment: EquipmentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin")),
):
    return create_equipment(db, equipment.name, equipment.status)
