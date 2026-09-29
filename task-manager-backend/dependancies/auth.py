
from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import Session

from core.security import oauth2_scheme, verify_access_token
from database import get_db
from models.user import User

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = verify_access_token(token)

    user = db.query(User).filter(User.username == username).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_UNAUTHORIZED, detail="User not found")

    return user
