import logging

import grpc
from sqlalchemy.orm.exc import NoResultFound

from .. import crud
from ..protos import blog_pb2
from ..protos import blog_pb2_grpc


logger = logging.getLogger(__name__)


class LikeBlogServicer(blog_pb2_grpc.BlogServicer):
    """Servicer to provide like methods that implements blog server."""

    def GetPostLikes(
        self,
        request: blog_pb2.GetPostLikesRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.GetPostLikesResponse:
        """
        Returns a list of like ids for a post with the given slug in the request.
        """
        logger.info("GetPostLikes")
        try:
            return blog_pb2.GetPostLikesResponse(
                likes=(
                    blog_pb2.LikeSchema(
                        post_id=like.post_id,
                        user_id=like.user_id,
                    )
                    for like in crud.get_post_likes_by_slug(request.post_slug)
                )
            )
        except NoResultFound:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

    def CreatePostLike(
        self,
        request: blog_pb2.CreatePostLikeRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.StatusResponse:
        """Creates a like for a post with the given slug in the request."""
        logger.info("CreatePostLike")
        crud.create_like(request.like)
        return blog_pb2.StatusResponse(status="OK")

    def DeletePostLike(
        self,
        request: blog_pb2.DeletePostLikeRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.StatusResponse:
        """Deletes a like by the like id in the request."""
        logger.info("DeletePostLike")
        try:
            crud.delete_like(request.like_id)
            return blog_pb2.StatusResponse(status="OK")
        except NoResultFound:
            context.abort(grpc.StatusCode.NOT_FOUND, "Like not found")