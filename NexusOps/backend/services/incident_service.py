
from sqlalchemy.orm import Session
from database_models import IncidentDB
from services.equipment_service import get_equipment_by_id


def get_all_incidents(db: Session):
    return db.query(IncidentDB).all()


def get_incident_by_id(db: Session, incident_id: int):
    return db.query(IncidentDB).filter(IncidentDB.id == incident_id).first()


def create_incident(
    db: Session,
    title: str,
    severity: str,
    status: str,
    equipment_id: int
):
    if get_equipment_by_id(db, equipment_id) is None:
        return None

    incident = IncidentDB(
        title=title,
        severity=severity,
        status=status,
        equipment_id=equipment_id
    )

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident


def update_incident(
    db: Session,
    incident_id: int,
    title: str,
    severity: str,
    status: str,
    equipment_id: int
):
    incident = get_incident_by_id(db, incident_id)

    if incident is None:
        return None

    if get_equipment_by_id(db, equipment_id) is None:
        return None

    incident.title = title
    incident.severity = severity
    incident.status = status
    incident.equipment_id = equipment_id

    db.commit()
    db.refresh(incident)

    return incident


def delete_incident(db: Session, incident_id: int):
    incident = get_incident_by_id(db, incident_id)

    if incident is None:
        return False

    db.delete(incident)
    db.commit()

    return True
