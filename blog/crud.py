import logging
from typing import Optional, NoReturn

from sqlalchemy import update
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session, joinedload

import models
from blog import services
from blog.protos import blog_pb2 as schemas
from auth.exc import AccessDenied
from db import SessionLocal, add_commit_and_refresh


logger = logging.getLogger(__name__)


# * C - create ----------------------------------------------------------------


def create_post(
    post_schema: schemas.PostCreateSchema, current_user_id: int
) -> models.Post:
    """Creates post in database and returns it."""
    with SessionLocal() as db:
        post = models.Post(
            title=post_schema.title,
            body=post_schema.body,
            user_id=current_user_id,
        )
        post.tags = services.get_all_tags_for_post_from_(post_schema.tags, db)
        return add_commit_and_refresh(db, post)


def create_comment(
    comment_schema: schemas.CommentCreateSchema, current_user_id: int
) -> models.Comment:
    """Creates comment in database and returns it."""
    with SessionLocal() as db:
        comment = models.Comment(
            body=comment_schema.body,
            user_id=current_user_id,
            post_id=comment_schema.post_id,
        )
        return add_commit_and_refresh(db, comment)


def create_like(post_id: int, current_user_id: int) -> models.Like:
    """Creates like in database and returns it."""
    with SessionLocal() as db:
        like = models.Like(user_id=current_user_id, post_id=post_id)
        return add_commit_and_refresh(db, like)


# * R - read ------------------------------------------------------------------


def get_all_posts(limit: int, offset: int) -> list[models.Post]:
    """Returns all posts from database."""
    with SessionLocal() as db:
        return (
            db.query(models.Post)
            .order_by(models.Post.id.desc())
            .options(joinedload(models.Post.tags))
            .limit(limit)
            .offset(offset)
            .all()
        )


def get_all_tags(limit: int, offset: int) -> list[models.Tag]:
    """Returns all tags from database."""
    with SessionLocal() as db:
        return db.query(models.Tag).limit(limit).offset(offset).all()


def get_post_by_slug(slug: str, db: Optional[Session] = None) -> models.Post:
    """Returns post from database by slug."""
    if db is None:
        logger.debug("DB session is None in get_post_by_slug")
        db = SessionLocal()
    post = (
        db.query(models.Post)
        .filter(models.Post.slug == slug)
        .options(joinedload(models.Post.tags))
        .first()
    )
    db.close()
    if post is None:
        raise NoResultFound
    return post


def get_tag_by_slug(slug: str) -> models.Tag:
    """Returns tag from database by slug."""
    with SessionLocal() as db:
        tag = (
            db.query(models.Tag)
            .filter(models.Tag.slug == slug)
            .options(joinedload(models.Tag.posts))
            .first()
        )
        if tag is None:
            raise NoResultFound
        return tag


def get_post_comments_by_slug(slug: str) -> list[models.Comment]:
    """Returns post comments from database by slug."""
    with SessionLocal() as db:
        post = get_post_by_slug(slug, db)
        return (
            db.query(models.Comment)
            .filter(models.Comment.post_id == post.id)
            .all()
        )


def get_post_likes_by_slug(slug: str) -> list[models.Like]:
    """Returns post likes from database by slug."""
    with SessionLocal() as db:
        post = get_post_by_slug(slug, db)
        return (
            db.query(models.Like).filter(models.Like.post_id == post.id).all()
        )


def _get_comment_by_id(db: Session, comment_id: int) -> models.Comment:
    """Returns comment from database by id."""
    comment = (
        db.query(models.Comment)
        .filter(models.Comment.id == comment_id)
        .first()
    )
    if comment is None:
        raise NoResultFound
    return comment


# * U - update ----------------------------------------------------------------


def check_if_current_user_is_owner(
    object_user_id: int, current_user_id: int
) -> None | NoReturn:
    """Checks if current user is owner of object."""
    if not object_user_id == current_user_id:
        raise AccessDenied


def update_post(
    slug: str,
    post_update_schema: schemas.PostUpdateSchema,
    current_user_id: int,
) -> models.Post:
    """Updates post in database and returns it."""
    with SessionLocal() as db:
        post = get_post_by_slug(slug, db)
        check_if_current_user_is_owner(post.user_id, current_user_id)
        db.execute(
            update(models.Post)
            .where(models.Post.slug == slug)
            .values(
                title=post_update_schema.title,
                body=post_update_schema.body,
                # tags=services.get_all_tags_for_post_from_(
                #     post_update_schema.tags, db
                # ),
            )
        )
        db.commit()


def update_comment(
    comment_update_schema: schemas.CommentUpdateSchema,
    current_user_id: int,
) -> models.Comment:
    """Updates comment in database and returns it."""
    with SessionLocal() as db:
        comment = _get_comment_by_id(db, comment_update_schema.id)
        check_if_current_user_is_owner(comment.user_id, current_user_id)
        db.execute(
            update(models.Comment)
            .where(models.Comment.id == comment_update_schema.id)
            .values(body=comment_update_schema.body)
        )
        db.commit()


# * D - delete ----------------------------------------------------------------


def _delete_and_commit(db: Session, model: models.Base) -> models.Base:
    """Deletes model from database and returns it."""
    db.delete(model)
    db.commit()
    return model


def delete_post(slug: str, current_user_id: int) -> models.Post:
    """Deletes post from database and returns it."""
    with SessionLocal() as db:
        post = get_post_by_slug(slug, db)
        check_if_current_user_is_owner(post.user_id, current_user_id)
        return _delete_and_commit(db, post)


def delete_comment(comment_id: int, current_user_id: int) -> models.Comment:
    """Deletes comment from database and returns it."""
    with SessionLocal() as db:
        comment = _get_comment_by_id(db, comment_id)
        check_if_current_user_is_owner(comment.user_id, current_user_id)
        return _delete_and_commit(db, comment)


def delete_like(like_id: int, current_user_id: int) -> models.Like:
    """Deletes like from database and returns it."""
    with SessionLocal() as db:
        like = db.query(models.Like).filter(models.Like.id == like_id).first()
        if like is None:
            raise NoResultFound
        check_if_current_user_is_owner(like.user_id, current_user_id)
        return _delete_and_commit(db, like)
