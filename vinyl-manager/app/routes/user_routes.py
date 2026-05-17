from fastapi import APIRouter, Depends

from app.core.database import get_db
from app.schemas.user import UserCreate, LoginRequest
from app.controllers.user_controller import register, login

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", status_code=201)
def register_route(payload: UserCreate, db=Depends(get_db)):
    return register(db, payload.username, payload.email, payload.password)


@router.post("/login")
def login_route(payload: LoginRequest, db=Depends(get_db)):
    return login(db, payload.username, payload.password)
