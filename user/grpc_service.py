import grpc
from concurrent import futures

from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
from grpc_reflection.v1alpha import reflection

import user.protos.user_pb2 as user_pb2
import user.protos.user_pb2_grpc as user_pb2_grpc


class UserServicer(user_pb2_grpc.UserServicer):
    """Servicer to provide user methods that implements user server."""


async def start(address: str):
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

    try:
        await server.wait_for_termination()
    except KeyboardInterrupt or RuntimeError:
        await server.stop(0)
