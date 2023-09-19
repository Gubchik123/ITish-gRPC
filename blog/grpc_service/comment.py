import logging

import grpc

from models import User, Comment
from decorators import catch_not_found_
from auth.decorators import login_required

from .. import crud
from ..protos import blog_pb2
from ..protos import blog_pb2_grpc


logger = logging.getLogger(__name__)


class CommentBlogServicer(blog_pb2_grpc.BlogServicer):
    """Servicer to provide comment methods that implements blog server."""

    @catch_not_found_("Post")
    def GetPostComments(
        self,
        request: blog_pb2.GetPostCommentsRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.GetPostCommentsResponse:
        """
        Returns a list of comments for a post with the given slug in the request.
        """
        logger.info("GetPostComments")
        return blog_pb2.GetPostCommentsResponse(
            comments=(
                self._get_comment_schema_from_(comment)
                for comment in crud.get_post_comments_by_slug(
                    request.post_slug
                )
            )
        )

    @login_required
    def CreatePostComment(
        self,
        request: blog_pb2.CreatePostCommentRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> blog_pb2.StatusResponse:
        """Creates a comment for a post with the given slug in the request."""
        logger.info("CreatePostComment")
        crud.create_comment(request.comment, current_user.id)
        return blog_pb2.StatusResponse(status="OK")

    @login_required
    @catch_not_found_("Comment")
    def UpdatePostComment(
        self,
        request: blog_pb2.UpdatePostCommentRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> blog_pb2.StatusResponse:
        """Updates a comment by the comment id in the request."""
        logger.info("UpdatePostComment")
        crud.update_comment(request.comment, current_user.id)
        return blog_pb2.StatusResponse(status="OK")

    @login_required
    @catch_not_found_("Comment")
    def DeletePostComment(
        self,
        request: blog_pb2.DeletePostCommentRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> blog_pb2.StatusResponse:
        """Deletes a comment by the comment id in the request."""
        logger.info("DeletePostComment")
        crud.delete_comment(request.comment_id, current_user.id)
        return blog_pb2.StatusResponse(status="OK")

    @staticmethod
    def _get_comment_schema_from_(comment: Comment) -> blog_pb2.CommentSchema:
        """Returns a CommentSchema from the given Comment model."""
        return blog_pb2.CommentSchema(
            body=comment.body,
            user_id=comment.user_id,
            post_id=comment.post_id,
        )
