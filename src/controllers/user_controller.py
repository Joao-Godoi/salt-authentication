from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..core.security import hash_password, verify_password
from ..models.user import User
from ..schemas.user import CreateUserSerializer, LoginSerializer


def register_user(user: CreateUserSerializer, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already registered")

    password_hash = hash_password(user.password)
    db_user = User(username=user.username, password_hash=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def login_user(user: LoginSerializer, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}


def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()
