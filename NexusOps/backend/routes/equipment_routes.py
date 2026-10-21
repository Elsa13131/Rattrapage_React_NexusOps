from fastapi import APIRouter
from services.equipment_service import get_all_equipments

router = APIRouter()


@router.get("/equipments")
def get_equiments():
    return get_all_equipments()