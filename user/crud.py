import logging
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from sqlalchemy.orm.exc import NoResultFound

import models
from db import SessionLocal
from auth.utils import get_hashed_password

from .protos.user_pb2 import UserSchema


logger = logging.getLogger(__name__)


def get_user_by_(username: str, db: Optional[Session] = None):
    """Returns user from database by the given username."""
    if db is None:
        logger.debug("DB session is None in get_user_by_(username)")
        db = SessionLocal()
    user = db.query(models.User).filter_by(username=username).first()
    db.close()
    if user is None:
        raise NoResultFound
    return user


def get_user_posts_by_(user_username: str, limit: int, offset: int):
    """Returns user posts from database by the given username."""
    with SessionLocal() as db:
        user = get_user_by_(user_username, db)
        return (
            db.query(models.Post)
            .filter_by(user_id=user.id)
            .limit(limit)
            .offset(offset)
            .all()
        )


def get_user_comments_by_(user_username: str, limit: int, offset: int):
    """Returns user comments from database by the given username."""
    with SessionLocal() as db:
        user = get_user_by_(user_username, db)
        return (
            db.query(models.Comment)
            .filter_by(user_id=user.id)
            .limit(limit)
            .offset(offset)
            .all()
        )


def get_user_liked_posts_by_(user_username: str, limit: int, offset: int):
    """Returns user liked posts from database by the given username."""
    with SessionLocal() as db:
        user = get_user_by_(user_username, db)
        user_liked_posts_ids = (
            like.post_id
            for like in db.query(models.Like).filter_by(user_id=user.id).all()
        )
        return (
            db.query(models.Post)
            .filter(models.Post.id.in_(user_liked_posts_ids))
            .limit(limit)
            .offset(offset)
            .all()
        )


def update_user_with_(username: str, user_schema: UserSchema):
    """Updates user in database by the given username."""
    with SessionLocal() as db:
        user = get_user_by_(username, db)
        db.execute(
            update(models.User)
            .where(models.User.username == username)
            .values(
                username=user_schema.username or user.username,
                email=user_schema.email or user.email,
                password=user.password
                if not user_schema.password or len(user_schema.password) == 60
                else get_hashed_password(user_schema.password),
            )
        )
        db.commit()


def delete_user_with_(username: str):
    """Deletes user from database by the given username."""
    with SessionLocal() as db:
        db.execute(delete(models.User).where(models.User.username == username))
        db.commit()
