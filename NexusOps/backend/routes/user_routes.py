
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
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
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    return user


@router.post("/users", status_code=201)
def post_user(user: User, db: Session = Depends(get_db)):
    return create_user(db, user.name, user.email, user.role)


@router.put("/users/{user_id}")
def put_user(user_id: int, user: User, db: Session = Depends(get_db)):
    updated_user = update_user(
        db,
        user_id,
        user.name,
        user.email,
        user.role
    )

    if updated_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    return updated_user


@router.delete("/users/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    deleted = delete_user(db, user_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Utilisateur introuvable")

    return {"message": "Utilisateur supprimé"}
