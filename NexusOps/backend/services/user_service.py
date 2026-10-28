
from sqlalchemy.orm import Session
from database_models import UserDB


def get_all_users(db: Session):
    return db.query(UserDB).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(UserDB).filter(UserDB.id == user_id).first()


def create_user(db: Session, name: str, email: str, role: str):
    user = UserDB(name=name, email=email, role=role)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_user(db: Session, user_id: int, name: str, email: str, role: str):
    user = get_user_by_id(db, user_id)

    if user is None:
        return None

    user.name = name
    user.email = email
    user.role = role

    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    if user is None:
        return False

    db.delete(user)
    db.commit()

    return True
