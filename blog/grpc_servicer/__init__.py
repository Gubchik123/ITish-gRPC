import logging

import grpc
from concurrent import futures
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_reflection.v1alpha import reflection

from .post import PostBlogServicer
from .tag import TagBlogServicer
from .comment import CommentBlogServicer
from .like import LikeBlogServicer

from ..protos import blog_pb2
from ..protos import blog_pb2_grpc


logger = logging.getLogger(__name__)


class BlogServicer(
    PostBlogServicer,
    TagBlogServicer,
    CommentBlogServicer,
    LikeBlogServicer,
    blog_pb2_grpc.BlogServicer,
):
    """Servicer to provide blog methods that implements blog server."""


async def start(address: str):
    """Starts Blog gRPC server."""
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
