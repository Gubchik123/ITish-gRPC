import logging

import grpc
from concurrent import futures
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_reflection.v1alpha import reflection

from models import User
from decorators import catch_not_found_
from auth.decorators import login_required
from blog.protos.blog_pb2 import StatusResponse
from blog.grpc_servicer import PostBlogServicer, CommentBlogServicer

from . import crud
from .protos import user_pb2
from .protos import user_pb2_grpc


logger = logging.getLogger(__name__)


class UserServicer(user_pb2_grpc.UserServicer):
    """Servicer to provide user methods that implements user server."""

    @login_required
    @catch_not_found_("User")
    def GetUserByUsername(
        self,
        request: user_pb2.GetUserByUsernameRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> user_pb2.GetUserByUsernameResponse:
        """Returns info about user by the given username in the request."""
        logger.info("GetUserByUsername")
        user = crud.get_user_by_(request.username)
        return user_pb2.GetUserByUsernameResponse(
            user=user_pb2.UserDetailSchema(
                id=user.id if user.id == current_user.id else None,
                username=user.username,
                email=user.email,
                created=user.created.strftime("%d.%m.%Y"),
            )
        )

    @login_required
    @catch_not_found_("User")
    def GetUserPosts(
        self,
        request: user_pb2.GetUserPostsRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> user_pb2.GetUserPostsResponse:
        """Returns user posts by the given username in the request."""
        logger.info("GetUserPosts")
        return user_pb2.GetUserPostsResponse(
            posts=(
                PostBlogServicer._get_post_list_schema_from_(post)
                for post in crud.get_user_posts_by_(
                    request.username, request.limit, request.offset
                )
            )
        )

    @login_required
    @catch_not_found_("User")
    def GetUserComments(
        self,
        request: user_pb2.GetUserCommentsRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> user_pb2.GetUserCommentsResponse:
        """Returns user comments by the given username in the request."""
        logger.info("GetUserComments")
        return user_pb2.GetUserCommentsResponse(
            comments=(
                CommentBlogServicer._get_comment_schema_from_(comment)
                for comment in crud.get_user_comments_by_(
                    request.username, request.limit, request.offset
                )
            )
        )

    @login_required
    @catch_not_found_("User")
    def GetUserLikedPosts(
        self,
        request: user_pb2.GetUserLikedPostsRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> user_pb2.GetUserLikedPostsResponse:
        """Returns user liked posts by the given username in the request."""
        logger.info("GetUserLikedPosts")
        return user_pb2.GetUserLikedPostsResponse(
            posts=(
                PostBlogServicer._get_post_list_schema_from_(post)
                for post in crud.get_user_liked_posts_by_(
                    request.username, request.limit, request.offset
                )
            )
        )

    @login_required
    def UpdateUser(
        self,
        request: user_pb2.UpdateUserRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> StatusResponse:
        """Updates current user by the given data in the request."""
        logger.info("UpdateUser")
        crud.update_user_with_(current_user.username, request.user)
        return StatusResponse(status="OK")

    @login_required
    def DeleteUser(
        self,
        request: user_pb2.DeleteUserRequest,
        context: grpc.ServicerContext,
        current_user: User,
    ) -> StatusResponse:
        """Deletes current user."""
        logger.info("DeleteUser")
        crud.delete_user_with_(current_user.username)
        return StatusResponse(status="OK")


async def start(address: str) -> None:
    """Starts User gRPC server."""
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=3))
    health_servicer = health.HealthServicer(
        experimental_non_blocking=True,
        experimental_thread_pool=futures.ThreadPoolExecutor(max_workers=3),
    )
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    SERVICES_NAMES = (
        user_pb2.DESCRIPTOR.services_by_name["User"].full_name,
        health.SERVICE_NAME,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICES_NAMES, server)
    for service in SERVICES_NAMES:
        health_servicer.set(service, health_pb2.HealthCheckResponse.SERVING)

    server.add_insecure_port(address)
    await server.start()

    logger.info(f"User gRPC server is listening on {address}")

    try:
        await server.wait_for_termination()
    except KeyboardInterrupt or RuntimeError:
        await server.stop(0)
