import logging

import grpc
from concurrent import futures

from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_reflection.v1alpha import reflection

from . import crud
from .protos import auth_pb2
from .protos import auth_pb2_grpc
from .utils import create_access_token_by_, create_refresh_token_by_


logger = logging.getLogger(__name__)


class AuthServicer(auth_pb2_grpc.AuthServicer):
    """Servicer to provide auth methods that implements auth server."""

    def Login(
        self, request: auth_pb2.LoginRequest, context: grpc.ServicerContext
    ) -> auth_pb2.LoginResponse:
        """Logins user and returns user id with JWT tokens."""
        logger.info("Login")
        user = crud.get_user_by_(request.email)
        if user is None or not user.is_valid_(request.password):
            context.abort(
                grpc.StatusCode.UNKNOWN, "Incorrect email or password"
            )
        return auth_pb2.LoginResponse(
            user_id=user.id,
            access_token=create_access_token_by_(user.email),
            refresh_token=create_refresh_token_by_(user.email),
        )

    def Signup(
        self, request: auth_pb2.SignupRequest, context: grpc.ServicerContext
    ) -> auth_pb2.SignupResponse:
        """Signups user and returns status."""
        logger.info("Signup")
        user = crud.get_user_with_(request.user)
        if user is not None:
            context.abort(
                grpc.StatusCode.ALREADY_EXISTS,
                "User with this email or username already exist",
            )
        crud.create_user(request.user)
        return auth_pb2.SignupResponse(status="OK")


async def start(address: str) -> None:
    """Starts Auth gRPC server."""
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=3))
    health_servicer = health.HealthServicer(
        experimental_non_blocking=True,
        experimental_thread_pool=futures.ThreadPoolExecutor(max_workers=3),
    )
    auth_pb2_grpc.add_AuthServicer_to_server(AuthServicer(), server)
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    SERVICES_NAMES = (
        auth_pb2.DESCRIPTOR.services_by_name["Auth"].full_name,
        health.SERVICE_NAME,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICES_NAMES, server)
    for service in SERVICES_NAMES:
        health_servicer.set(service, health_pb2.HealthCheckResponse.SERVING)

    server.add_insecure_port(address)
    await server.start()

    logger.info(f"Auth gRPC server is listening on {address}")

    try:
        await server.wait_for_termination()
    except KeyboardInterrupt or RuntimeError:
        await server.stop(0)
