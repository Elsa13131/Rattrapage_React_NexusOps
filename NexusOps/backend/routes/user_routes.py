from fastapi import APIRouter, HTTPException
from models.user import User
from services.user_service import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user
)

router = APIRouter()


@router.get("/users")
def get_users():
    return get_all_users()


@router.get("/users/{user_id}")
def get_user(user_id: int):
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    return user


@router.post("/users")
def post_user(user: User):
    return create_user(user.name, user.email, user.role)


@router.put("/users/{user_id}")
def put_user(user_id: int, user: User):
    updated_user = update_user(
        user_id,
        user.name,
        user.email,
        user.role
    )

    if updated_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    return updated_user


@router.delete("/users/{user_id}")
def remove_user(user_id: int):
    deleted = delete_user(user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    return {"message": "Utilisateur supprimé"}