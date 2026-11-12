
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models.incident import Incident
from database import get_db
from services.auth_dependencies import get_current_user, require_roles
from services.incident_service import (
    get_all_incidents,
    get_incident_by_id,
    create_incident,
    update_incident,
    delete_incident
)

router = APIRouter()


@router.get("/incidents")
def get_incidents(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_all_incidents(db)


@router.get("/incidents/{incident_id}")
def get_incident(
    incident_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    incident = get_incident_by_id(db, incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident introuvable"
        )

    return incident


@router.post("/incidents", status_code=201)
def post_incident(
    incident: Incident,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin", "operator"))
):
    new_incident = create_incident(
        db,
        incident.title,
        incident.severity,
        incident.status,
        incident.equipment_id
    )

    if new_incident is None:
        raise HTTPException(
            status_code=404,
            detail="Équipement introuvable"
        )

    return new_incident


@router.put("/incidents/{incident_id}")
def put_incident(
    incident_id: int,
    incident: Incident,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin", "operator"))
):
    updated_incident = update_incident(
        db,
        incident_id,
        incident.title,
        incident.severity,
        incident.status,
        incident.equipment_id
    )

    if updated_incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident ou équipement introuvable"
        )

    return updated_incident


@router.delete("/incidents/{incident_id}")
def remove_incident(
    incident_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin"))
):
    deleted = delete_incident(db, incident_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Incident introuvable"
        )

    return {"message": "Incident supprimé"}
