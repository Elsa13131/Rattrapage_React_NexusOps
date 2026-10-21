incidents = [
    {
        "id": 1,
        "title": "Serveur indisponible",
        "severity": "high",
        "status": "open",
        "equipment_id": 1
    }
]


def get_all_incidents():
    return incidents


def get_incident_by_id(incident_id: int):
    for incident in incidents:
        if incident["id"] == incident_id:
            return incident

    return None


def create_incident(title: str, severity: str, status: str, equipment_id: int):
    new_id = max(incident["id"] for incident in incidents) + 1

    new_incident = {
        "id": new_id,
        "title": title,
        "severity": severity,
        "status": status,
        "equipment_id": equipment_id
    }

    incidents.append(new_incident)

    return new_incident

def update_incident(
    incident_id: int,
    title: str,
    severity: str,
    status: str,
    equipment_id: int
):
    incident = get_incident_by_id(incident_id)

    if incident is None:
        return None

    incident["title"] = title
    incident["severity"] = severity
    incident["status"] = status
    incident["equipment_id"] = equipment_id

    return incident


def delete_incident(incident_id: int):
    incident = get_incident_by_id(incident_id)

    if incident is None:
        return False

    incidents.remove(incident)

    return True