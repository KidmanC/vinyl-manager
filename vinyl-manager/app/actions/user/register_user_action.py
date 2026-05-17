from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.user_model import User
from app.core.security import hash_password


def execute(db: Session, username: str, email: str, password: str) -> User:
    existing = db.query(User).filter(
        (User.username == username) | (User.email == email)
    ).first()
    if existing:
        if existing.username == username:
            raise HTTPException(status_code=409, detail="Username already taken")
        raise HTTPException(status_code=409, detail="Email already registered")
    user = User(
        username=username,
        email=email,
        password_hash=hash_password(password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
