equipments = [
    {"id": 1, "name": "Serveur principal", "status": "online"},
    {"id": 2, "name": "PC accueil", "status": "offline"},
    {"id": 3, "name": "Switch réseau", "status": "online"}
]


def get_all_equipments():
    return equipments

def get_equipment_by_id(equipment_id: int):
    for equipment in equipments:
        if equipment["id"] == equipment_id:
            return equipment

    return None


def create_equipment(name: str, status: str):
    new_id = max(equipment["id"] for equipment in equipments) + 1

    new_equipment = {
        "id": new_id,
        "name": name,
        "status": status
    }

    equipments.append(new_equipment)

    return new_equipment

def update_equipment(equipment_id: int, name: str, status: str):
    equipment = get_equipment_by_id(equipment_id)

    if equipment is None:
        return None

    equipment["name"] = name
    equipment["status"] = status

    return equipment


def delete_equipment(equipment_id: int):
    equipment = get_equipment_by_id(equipment_id)

    if equipment is None:
        return False

    equipments.remove(equipment)

    return True