import logging

import grpc

import models
from decorators import catch_not_found_
from auth.decorators import login_required

from .. import crud
from ..protos import blog_pb2
from ..protos import blog_pb2_grpc


logger = logging.getLogger(__name__)


class PostBlogServicer(blog_pb2_grpc.BlogServicer):
    """Servicer to provide post methods that implements blog server."""

    def GetPosts(
        self, request: blog_pb2.GetPostsRequest, context: grpc.ServicerContext
    ) -> blog_pb2.GetPostsResponse:
        """Returns a list of posts."""
        logger.info("GetPosts")
        posts = crud.get_all_posts(request.limit, request.offset)
        return blog_pb2.GetPostsResponse(
            posts=(self._get_post_list_schema_from_(post) for post in posts)
        )

    @catch_not_found_("Post")
    def GetPostBySlug(
        self,
        request: blog_pb2.GetPostBySlugRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.GetPostBySlugResponse:
        """Returns a post by the given slug in the request."""
        logger.info("GetPostBySlug")
        post = crud.get_post_by_slug(request.slug)
        return blog_pb2.GetPostBySlugResponse(
            post=self._get_post_schema_from_(post)
        )

    @login_required
    def CreatePost(
        self,
        request: blog_pb2.CreatePostRequest,
        context: grpc.ServicerContext,
        current_user: models.User,
    ) -> blog_pb2.StatusResponse:
        """Creates a post by the given PostSchema in the request."""
        logger.info("CreatePost")
        crud.create_post(request.post, current_user.id)
        return blog_pb2.StatusResponse(status="OK")

    @login_required
    @catch_not_found_("Post")
    def UpdatePostBySlug(
        self,
        request: blog_pb2.UpdatePostBySlugRequest,
        context: grpc.ServicerContext,
        current_user: models.User,
    ) -> blog_pb2.StatusResponse:
        """Updates a post by the given PostUpdateSchema in the request."""
        logger.info("UpdatePostBySlug")
        crud.update_post(request.post_slug, request.post, current_user.id)
        return blog_pb2.StatusResponse(status="OK")

    @login_required
    @catch_not_found_("Post")
    def DeletePostBySlug(
        self,
        request: blog_pb2.DeletePostBySlugRequest,
        context: grpc.ServicerContext,
        current_user: models.User,
    ) -> blog_pb2.StatusResponse:
        """Deletes a post by the given slug in the request."""
        logger.info("DeletePostBySlug")
        crud.delete_post(request.slug, current_user.id)
        return blog_pb2.StatusResponse(status="OK")

    def _get_post_schema_from_(self, post: models.Post) -> blog_pb2.PostSchema:
        """Returns a PostSchema from the given Post model."""
        return blog_pb2.PostSchema(
            title=post.title,
            slug=post.slug,
            body=post.body,
            tags=(self._get_tag_schema_from_(tag) for tag in post.tags),
            user_id=post.user_id,
        )

    @staticmethod
    def _get_post_list_schema_from_(
        post: models.Post,
    ) -> blog_pb2.PostListSchema:
        """Returns a PostListSchema from the given Post model."""
        return blog_pb2.PostListSchema(
            title=post.title,
            slug=post.slug,
            user_id=post.user_id,
        )
