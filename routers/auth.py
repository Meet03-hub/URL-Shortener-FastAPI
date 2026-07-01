from fastapi import APIRouter
from fastapi import Depends
from fastapi import Header


from sqlalchemy.orm import Session

from dependencies import get_db

from schemas.user import UserRegister
from services.auth_service import register_user
from services.auth_service import get_all_users
from schemas.user import UserLogin
from services.auth_service import login_user
from dependencies import get_current_user


router = APIRouter()


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(
        db,
        user.username,
        user.email,
        user.password
    )

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(
        db,
        user.email,
        user.password
    )

@router.get("/users")
def get_users(
    db: Session = Depends(get_db)
):
    return get_all_users(db)

@router.get("/me")
def me(
    current_user=Depends(get_current_user)
):
    return current_user