from fastapi import APIRouter, HTTPException
from models.incident import Incident
from services.incident_service import (
    get_all_incidents,
    get_incident_by_id,
    create_incident,
    update_incident,
    delete_incident
)

router = APIRouter()


@router.get("/incidents")
def get_incidents():
    return get_all_incidents()


@router.get("/incidents/{incident_id}")
def get_incident(incident_id: int):
    incident = get_incident_by_id(incident_id)

    if incident is None:
        raise HTTPException(status_code=404, detail="Incident introuvable")

    return incident


@router.post("/incidents")
def post_incident(incident: Incident):
    return create_incident(
        incident.title,
        incident.severity,
        incident.status,
        incident.equipment_id
    )


@router.put("/incidents/{incident_id}")
def put_incident(incident_id: int, incident: Incident):
    updated_incident = update_incident(
        incident_id,
        incident.title,
        incident.severity,
        incident.status,
        incident.equipment_id
    )

    if updated_incident is None:
        raise HTTPException(status_code=404, detail="Incident introuvable")

    return updated_incident


@router.delete("/incidents/{incident_id}")
def remove_incident(incident_id: int):
    deleted = delete_incident(incident_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Incident introuvable")

    return {"message": "Incident supprimé"}