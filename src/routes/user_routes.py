from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..controllers.user_controller import list_users, login_user, register_user
from ..core.database import get_db
from ..schemas.user import CreateUserSerializer, LoginSerializer, UserResponse

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register(user: CreateUserSerializer, db: Session = Depends(get_db)):
    return register_user(user, db)


@router.post("/login")
def login(user: LoginSerializer, db: Session = Depends(get_db)):
    return login_user(user, db)


@router.get("/users", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return list_users(db)
