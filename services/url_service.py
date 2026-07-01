import random
import string
from fastapi import HTTPException

from models.url import URL


def generate_short_code():

    return ''.join(
        random.choices(
            string.ascii_letters +
            string.digits,
            k=6
        )
    )


def create_short_url(
    db,
    original_url,
    current_user
):

    short_code = generate_short_code()

    url = URL(
        original_url=original_url,
        short_code=short_code,
        user_id=int(current_user["sub"])
    )

    db.add(url)

    db.commit()

    db.refresh(url)

    return {
        "original_url": url.original_url,
        "short_code": url.short_code
    }

def get_url_by_code(
    db,
    short_code
):

    url = db.query(URL).filter(
        URL.short_code == short_code
    ).first()

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return url


def increment_clicks(
    db,
    url
):

    url.clicks += 1

    db.commit()

def get_url_analytics(
    db,
    short_code
):

    url = db.query(URL).filter(
        URL.short_code == short_code
    ).first()

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return {
        "original_url": url.original_url,
        "short_code": url.short_code,
        "clicks": url.clicks
    }
def get_my_urls(
    db,
    current_user
):

    urls = db.query(URL).filter(
        URL.user_id == int(current_user["sub"])
    ).all()

    return urls

def delete_url(
    db,
    short_code,
    current_user
):

    url = db.query(URL).filter(
        URL.short_code == short_code
    ).first()

    if not url:
        raise HTTPException(
            status_code=404,
            detail="URL not found"
        )

    if url.user_id != int(current_user["sub"]):
        raise HTTPException(
            status_code=403,
            detail="Not authorized"
        )

    db.delete(url)
    db.commit()

    return {
        "message": "URL deleted successfully"
    }