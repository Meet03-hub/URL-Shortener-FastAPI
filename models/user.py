from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        index=True
    )

    email = Column(
        String,
        unique=True,
        index=True
    )

    password = Column(String)
    urls = relationship(
        "URL",
        back_populates="owner"
    )