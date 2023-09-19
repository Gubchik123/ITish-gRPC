import logging

import grpc

from models import User
from decorators import catch_not_found_
from auth.decorators import login_required

from .. import crud
from ..protos import blog_pb2
from ..protos import blog_pb2_grpc


logger = logging.getLogger(__name__)


class LikeBlogServicer(blog_pb2_grpc.BlogServicer):
    """Servicer to provide like methods that implements blog server."""

    @catch_not_found_("Post")
    def GetPostLikes(
        self,
        request: blog_pb2.GetPostLikesRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.GetPostLikesResponse:
        """
        Returns a list of like ids for a post with the given slug in the request.
        """
        logger.info("GetPostLikes")
        return blog_pb2.GetPostLikesResponse(
            likes=(
                blog_pb2.LikeSchema(
                    post_id=like.post_id,
                    user_id=like.user_id,
                )
                for like in crud.get_post_likes_by_slug(request.post_slug)
            )
        )

    @login_required
    def CreatePostLike(
        self,
        request: blog_pb2.CreatePostLikeRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> blog_pb2.StatusResponse:
        """Creates a like for a post with the given slug in the request."""
        logger.info("CreatePostLike")
        crud.create_like(request.post_id, current_user.id)
        return blog_pb2.StatusResponse(status="OK")

    @login_required
    @catch_not_found_("Like")
    def DeletePostLike(
        self,
        request: blog_pb2.DeletePostLikeRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> blog_pb2.StatusResponse:
        """Deletes a like by the like id in the request."""
        logger.info("DeletePostLike")
        crud.delete_like(request.like_id, current_user.id)
        return blog_pb2.StatusResponse(status="OK")
