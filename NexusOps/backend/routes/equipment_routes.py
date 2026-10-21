from fastapi import APIRouter, HTTPException
from models.equipment import Equipment
from services.equipment_service import (
    get_all_equipments,
    get_equipment_by_id,
    create_equipment,
    update_equipment,
    delete_equipment

)

router = APIRouter()


@router.get("/equipments")
def get_equipments():
    return get_all_equipments()


@router.get("/equipments/{equipment_id}")
def get_equipment(equipment_id: int):
    equipment = get_equipment_by_id(equipment_id)

    if equipment is None:
        raise HTTPException(status_code=404, detail="Équipement introuvable")

    return equipment


@router.post("/equipments")
def post_equipment(equipment: Equipment):
    return create_equipment(equipment.name, equipment.status)

@router.put("/equipments/{equipment_id}")
def put_equipment(equipment_id: int, equipment: Equipment):
    updated_equipment = update_equipment(
        equipment_id,
        equipment.name,
        equipment.status
    )

    if updated_equipment is None:
        raise HTTPException(status_code=404, detail="Équipement introuvable")

    return updated_equipment


@router.delete("/equipments/{equipment_id}")
def remove_equipment(equipment_id: int):
    deleted = delete_equipment(equipment_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Équipement introuvable")

    return {"message": "Équipement supprimé"}