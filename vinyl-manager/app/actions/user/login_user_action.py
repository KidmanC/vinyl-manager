from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user_model import User
from app.core.security import verify_password, create_access_token


def execute(db: Session, username: str, password: str) -> str:
    user = db.query(User).filter(User.username == username).first()
    if user is None or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return create_access_token(data={"sub": str(user.id)})
