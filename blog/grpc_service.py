import logging

import grpc
from concurrent import futures
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_reflection.v1alpha import reflection
from sqlalchemy.orm.exc import NoResultFound

import models

from . import crud
from .protos import blog_pb2
from .protos import blog_pb2_grpc


logger = logging.getLogger(__name__)


class BlogServicer(blog_pb2_grpc.BlogServicer):
    """Servicer to provide blog methods that implements blog server."""

    # * Post methods ----------------------------------------------------------

    def GetPosts(
        self, request: blog_pb2.GetPostsRequest, context: grpc.ServicerContext
    ) -> blog_pb2.GetPostsResponse:
        """Returns a list of posts."""
        logger.info("GetPosts")
        posts = crud.get_all_posts(request.limit, request.offset)
        return blog_pb2.GetPostsResponse(
            posts=(self._get_post_list_schema_from_(post) for post in posts)
        )

    def GetPostBySlug(
        self,
        request: blog_pb2.GetPostBySlugRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.GetPostBySlugResponse:
        """Returns a post by the given slug in the request."""
        logger.info("GetPostBySlug")
        try:
            post = crud.get_post_by_slug(request.slug)
            return blog_pb2.GetPostBySlugResponse(
                post=self._get_post_schema_from_(post)
            )
        except NoResultFound:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

    def CreatePost(
        self,
        request: blog_pb2.CreatePostRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.StatusResponse:
        """Creates a post by the given PostSchema in the request."""
        logger.info("CreatePost")
        crud.create_post(request.post)
        return blog_pb2.StatusResponse(status="OK")

    def UpdatePostBySlug(
        self,
        request: blog_pb2.UpdatePostBySlugRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.StatusResponse:
        """Updates a post by the given PostUpdateSchema in the request."""
        logger.info("UpdatePostBySlug")
        try:
            crud.update_post(request.post_slug, request.post)
            return blog_pb2.StatusResponse(status="OK")
        except NoResultFound:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

    def DeletePostBySlug(
        self,
        request: blog_pb2.DeletePostBySlugRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.StatusResponse:
        """Deletes a post by the given slug in the request."""
        logger.info("DeletePostBySlug")
        try:
            crud.delete_post(request.slug)
            return blog_pb2.StatusResponse(status="OK")
        except NoResultFound:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

    def _get_post_schema_from_(self, post: models.Post) -> blog_pb2.PostSchema:
        """Returns a PostSchema from the given Post model."""
        return blog_pb2.PostSchema(
            title=post.title,
            slug=post.slug,
            body=post.body,
            tags=(self._get_tag_schema_from_(tag) for tag in post.tags),
            user_id=post.user_id,
        )

    def _get_post_list_schema_from_(
        self, post: models.Post
    ) -> blog_pb2.PostListSchema:
        """Returns a PostListSchema from the given Post model."""
        return blog_pb2.PostListSchema(
            title=post.title,
            slug=post.slug,
            user_id=post.user_id,
        )

    # * Tag methods -----------------------------------------------------------

    def GetTags(
        self, request: blog_pb2.GetTagsRequest, context: grpc.ServicerContext
    ) -> blog_pb2.GetTagsResponse:
        """Returns a list of tags."""
        logger.info("GetTags")
        tags = crud.get_all_tags(request.limit, request.offset)
        return blog_pb2.GetTagsResponse(
            tags=(self._get_tag_schema_from_(tag) for tag in tags)
        )

    def GetTagBySlug(
        self,
        request: blog_pb2.GetTagBySlugRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.GetTagBySlugResponse:
        """Returns a tag by slug."""
        logger.info("GetTagBySlug")
        try:
            tag = crud.get_tag_by_slug(request.slug)
        except NoResultFound:
            context.abort(grpc.StatusCode.NOT_FOUND, "Tag not found")
        return blog_pb2.GetTagBySlugResponse(
            tag=self._get_tag_schema_from_(tag),
            posts=(
                self._get_post_list_schema_from_(post) for post in tag.posts
            ),
        )

    def _get_tag_schema_from_(self, tag: models.Tag) -> blog_pb2.TagSchema:
        """Returns a TagSchema from the given Tag model."""
        return blog_pb2.TagSchema(
            title=tag.title,
            slug=tag.slug,
        )

    # * Comment methods -------------------------------------------------------

    def GetPostComments(
        self,
        request: blog_pb2.GetPostCommentsRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.GetPostCommentsResponse:
        """
        Returns a list of comments for a post with the given slug in the request.
        """
        logger.info("GetPostComments")
        try:
            return blog_pb2.GetPostCommentsResponse(
                comments=(
                    blog_pb2.CommentSchema(
                        body=comment.body,
                        user_id=comment.user_id,
                        post_id=comment.post_id,
                    )
                    for comment in crud.get_post_comments_by_slug(
                        request.post_slug
                    )
                )
            )
        except NoResultFound:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

    def CreatePostComment(
        self,
        request: blog_pb2.CreatePostCommentRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.StatusResponse:
        """Creates a comment for a post with the given slug in the request."""
        logger.info("CreatePostComment")
        crud.create_comment(request.comment)
        return blog_pb2.StatusResponse(status="OK")

    def UpdatePostComment(
        self,
        request: blog_pb2.UpdatePostCommentRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.StatusResponse:
        """Updates a comment by the comment id in the request."""
        logger.info("UpdatePostComment")
        try:
            crud.update_comment(request.comment)
            return blog_pb2.StatusResponse(status="OK")
        except NoResultFound:
            context.abort(grpc.StatusCode.NOT_FOUND, "Comment not found")

    def DeletePostComment(
        self,
        request: blog_pb2.DeletePostCommentRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.StatusResponse:
        """Deletes a comment by the comment id in the request."""
        logger.info("DeletePostComment")
        try:
            crud.delete_comment(request.comment_id)
            return blog_pb2.StatusResponse(status="OK")
        except NoResultFound:
            context.abort(grpc.StatusCode.NOT_FOUND, "Comment not found")

    # * Like methods ----------------------------------------------------------

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


async def start(address: str):
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=3))
    health_servicer = health.HealthServicer(
        experimental_non_blocking=True,
        experimental_thread_pool=futures.ThreadPoolExecutor(max_workers=3),
    )
    blog_pb2_grpc.add_BlogServicer_to_server(BlogServicer(), server)
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    SERVICES_NAMES = (
        blog_pb2.DESCRIPTOR.services_by_name["Blog"].full_name,
        health.SERVICE_NAME,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICES_NAMES, server)
    for service in SERVICES_NAMES:
        health_servicer.set(service, health_pb2.HealthCheckResponse.SERVING)

    server.add_insecure_port(address)
    await server.start()

    logger.info(f"Blog gRPC server is listening on {address}")

    try:
        await server.wait_for_termination()
    except KeyboardInterrupt or RuntimeError:
        await server.stop(0)
