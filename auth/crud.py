from sqlalchemy.orm.exc import NoResultFound

from models import User
from db import SessionLocal, add_commit_and_refresh

from .protos.auth_pb2 import UserSchema


def get_user_with_(user_schema: UserSchema):
    """Returns user by email and username in the given UserSchema."""
    with SessionLocal() as db:
        user = (
            db.query(User)
            .filter(
                User.email == user_schema.email,
                User.username == user_schema.username,
            )
            .first()
        )
    if user is None:
        raise NoResultFound
    return user


def get_user_by_(email: str):
    """Returns user by the given email."""
    with SessionLocal() as db:
        user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise NoResultFound
    return user


def create_user(user_schema: UserSchema):
    """Creates and returns user by data in the given UserSchema."""
    with SessionLocal() as db:
        return add_commit_and_refresh(
            db, 
            User(
                username=user_schema.username,
                email=user_schema.email,
                password=user_schema.password,
            )
        )
