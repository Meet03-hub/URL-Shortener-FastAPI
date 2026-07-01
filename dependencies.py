from database import SessionLocal
from fastapi import Header
from fastapi import HTTPException

from security import verify_token
from typing import Optional


def get_current_user(
    authorization: Optional[str] = Header(
        default=None,
        alias="Authorization"
    )
):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Token missing"
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    payload = verify_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()