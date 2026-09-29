
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.user import User
from core.security import hash_password, verify_password

def create_user(db: Session, username: str, password: str):
    existing_user = db.query(User).filter(User.username == username).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(username=username, hashed_password=hash_password(password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        return None

    if len(password) > 72:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user
