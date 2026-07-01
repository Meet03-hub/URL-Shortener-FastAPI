from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from dependencies import get_current_user, get_db

from schemas.url import URLCreate

from services.url_service import create_short_url

from fastapi.responses import RedirectResponse

from services.url_service import (
    create_short_url,
    get_url_by_code,
    increment_clicks,
    get_url_analytics,
    get_my_urls,
    delete_url
)

router = APIRouter()


@router.post("/shorten")
def shorten(
    url: URLCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_short_url(
        db,
        url.original_url,
        current_user
    )

@router.get("/my-urls")
def my_urls(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return get_my_urls(
        db,
        current_user
    )

@router.get("/{short_code}")
def redirect_url(
    short_code: str,
    db: Session = Depends(get_db)
):

    url = get_url_by_code(
        db,
        short_code
    )

    increment_clicks(
        db,
        url
    )

    return RedirectResponse(
        url.original_url
    )

@router.get("/analytics/{short_code}")
def analytics(
    short_code: str,
    db: Session = Depends(get_db)
):

    return get_url_analytics(
        db,
        short_code
    )

@router.delete("/delete/{short_code}")
def delete(
    short_code: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return delete_url(
        db,
        short_code,
        current_user
    )