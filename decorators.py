from functools import wraps
from typing import Callable

import grpc
from google.protobuf.message import Message
from sqlalchemy.orm.exc import NoResultFound


def catch_not_found_(model: str) -> Callable:
    """Decorator for RPC methods to catch model not found exception."""

    def wrapper(rpc_method: Callable) -> Callable:
        @wraps(rpc_method)
        def inner(
            servicer_instance,
            request: Message,
            context: grpc.ServicerContext,
            *args,
        ):
            """Catches model not found exception
            and aborts with NOT_FOUND gRPC status code."""
            try:
                return rpc_method(servicer_instance, request, context, *args)
            except NoResultFound:
                context.abort(grpc.StatusCode.NOT_FOUND, f"{model} not found")

        return inner

    return wrapper
