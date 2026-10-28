
from sqlalchemy.orm import Session
from database_models import EquipmentDB


def get_all_equipments(db: Session):
    return db.query(EquipmentDB).all()


def get_equipment_by_id(db: Session, equipment_id: int):
    return db.query(EquipmentDB).filter(EquipmentDB.id == equipment_id).first()


def create_equipment(db: Session, name: str, status: str):
    equipment = EquipmentDB(name=name, status=status)
    db.add(equipment)
    db.commit()
    db.refresh(equipment)
    return equipment


def update_equipment(db: Session, equipment_id: int, name: str, status: str):
    equipment = get_equipment_by_id(db, equipment_id)

    if equipment is None:
        return None

    equipment.name = name
    equipment.status = status
    db.commit()
    db.refresh(equipment)

    return equipment


def delete_equipment(db: Session, equipment_id: int):
    equipment = get_equipment_by_id(db, equipment_id)

    if equipment is None:
        return False

    db.delete(equipment)
    db.commit()

    return True
