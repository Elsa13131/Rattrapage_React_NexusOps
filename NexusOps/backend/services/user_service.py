users = [
    {"id": 1, "name": "Elsa", "email": "elsa@example.com", "role": "admin"},
    {"id": 2, "name": "Thomas", "email": "thomas@example.com", "role": "operator"},
    {"id": 3, "name": "Julie", "email": "julie@example.com", "role": "viewer"}
]


def get_all_users():
    return users


def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    return None


def create_user(name: str, email: str, role: str):
    new_id = max((user["id"] for user in users), default=0) + 1

    new_user = {
        "id": new_id,
        "name": name,
        "email": email,
        "role": role
    }

    users.append(new_user)

    return new_user


def update_user(user_id: int, name: str, email: str, role: str):
    user = get_user_by_id(user_id)

    if user is None:
        return None

    user["name"] = name
    user["email"] = email
    user["role"] = role

    return user


def delete_user(user_id: int):
    user = get_user_by_id(user_id)

    if user is None:
        return False

    users.remove(user)

    return True