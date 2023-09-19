from models import User
from db import SessionLocal, add_commit_and_refresh

from user.protos.user_pb2 import UserSchema


def get_user_with_(user_schema: UserSchema) -> User:
    """Returns user by email and username in the given UserSchema."""
    with SessionLocal() as db:
        return (
            db.query(User)
            .filter(
                User.email == user_schema.email,
                User.username == user_schema.username,
            )
            .first()
        )


def get_user_by_(email: str) -> User:
    """Returns user by the given email."""
    with SessionLocal() as db:
        return db.query(User).filter(User.email == email).first()


def create_user(user_schema: UserSchema) -> User:
    """Creates and returns user by data in the given UserSchema."""
    with SessionLocal() as db:
        return add_commit_and_refresh(
            db,
            User(
                username=user_schema.username,
                email=user_schema.email,
                password=user_schema.password,
            ),
        )
