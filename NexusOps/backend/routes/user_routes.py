
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from database_models import UserDB
from models.user import User
from models.user_create import UserCreate
from services.auth_service import hash_password
from services.auth_dependencies import require_roles
from services.user_service import (
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user,
)

router = APIRouter()


@router.get("/users", response_model=list[User])
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin")),
):
    return get_all_users(db)


@router.get("/users/{user_id}", response_model=User)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin")),
):
    user = get_user_by_id(db, user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur introuvable",
        )

    return user


@router.post("/users", status_code=201, response_model=User)
def post_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin")),
):
    existing_user = (
        db.query(UserDB)
        .filter(UserDB.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Cette adresse email est déjà utilisée",
        )

    new_user = UserDB(
        name=user.name,
        email=user.email,
        role=user.role,
        password_hash=hash_password(user.password),
    )

    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)
    except Exception:
        db.rollback()
        raise

    return new_user


@router.put("/users/{user_id}", response_model=User)
def put_user(
    user_id: int,
    user: User,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin")),
):
    updated_user = update_user(
        db,
        user_id,
        user.name,
        user.email,
        user.role,
    )

    if updated_user is None:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur introuvable",
        )

    return updated_user


@router.delete("/users/{user_id}")
def remove_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles("admin")),
):
    deleted = delete_user(db, user_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Utilisateur introuvable",
        )

    return {"message": "Utilisateur supprimé"}
