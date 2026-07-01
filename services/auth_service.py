from models.user import User
from security import hash_password
from security import verify_password
from security import create_access_token


def register_user(
    db,
    username,
    email,
    password
):
    hashed_password = hash_password(password)

    user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return {
        "message": "User Registered Successfully",
        "id": user.id,
        "username": user.username,
        "email": user.email
    }

def login_user(
    db,
    email,
    password
):
    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return {
            "message": "User not found"
        }

    if not verify_password(
        password,
        user.password
    ):
        return {
            "message": "Invalid password"
        }

    access_token = create_access_token(
    {
        "sub": str(user.id),
        "email": user.email
    }
)

    return {
    "access_token": access_token,
    "token_type": "bearer"
}


def get_all_users(db):
    return db.query(User).all()