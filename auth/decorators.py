from functools import wraps
from typing import Callable

import grpc
from google.protobuf.message import Message

from .utils import verify_
from .crud import get_user_by_


def login_required(rpc_method: Callable):
    """Decorator for RPC methods that require login."""

    @wraps(rpc_method)
    def wrapper(self, request: Message, context: grpc.ServicerContext):
        """Checks if user is logged in and returns user instance."""
        token = None
        try:
            token = _get_token_from_(context.invocation_metadata())
        except IndexError:
            context.abort(
                grpc.StatusCode.UNAUTHENTICATED, "Missing authorization header"
            )
            return

        if token is None:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Missing token")
            return

        verified_result = verify_(token)

        if verified_result["error"] is not None:
            context.abort(
                grpc.StatusCode.UNAUTHENTICATED, verified_result["error"]
            )
            return
        request.user_id = get_user_by_(verified_result["email"]).id
        return rpc_method(self, request, context)

    return wrapper


def _get_token_from_(invocation_metadata: tuple) -> str | None:
    authorization_metadata = list(
        filter(
            lambda x: x.key == "authorization",
            invocation_metadata,
        )
    )[0]
    return authorization_metadata.value.split(" ")[1]  # Remove "Bearer "
