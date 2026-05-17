from sqlalchemy.orm import Session

from app.actions.user.login_user_action import execute as login_user
from app.actions.user.register_user_action import execute as register_user
from app.schemas.user import Token, UserResponse


def register(db: Session, username: str, email: str, password: str) -> UserResponse:
    user = register_user(db, username, email, password)
    return UserResponse(id=user.id, username=user.username, email=user.email)


def login(db: Session, username: str, password: str) -> Token:
    access_token = login_user(db, username, password)
    return Token(access_token=access_token, token_type="bearer")
