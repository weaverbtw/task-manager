
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.user import User
from database import get_db
from schemas.user import UserCreate, UserResponse
import crud.user as crud

router = APIRouter(prefix="/users", tags=["User"])

@router.post("", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user.username, user.password)

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user_by_id(db, user_id)