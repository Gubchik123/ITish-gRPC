from functools import wraps
from typing import Callable

import grpc
from google.protobuf.message import Message

from .exc import AccessDenied
from .utils import verify_
from .crud import get_user_by_


def login_required(rpc_method: Callable) -> Callable:
    """Decorator for RPC methods that require login."""

    @wraps(rpc_method)
    def wrapper(
        servicer_instance, request: Message, context: grpc.ServicerContext
    ):
        """Checks if user is logged in and returns user instance."""
        try:
            token = _get_token_from_(context.invocation_metadata())
        except IndexError:
            context.abort(
                grpc.StatusCode.UNAUTHENTICATED, "Missing authorization token"
            )
            return

        verified_result = verify_(token)

        if verified_result["error"] is not None:
            context.abort(
                grpc.StatusCode.UNAUTHENTICATED, verified_result["error"]
            )
            return
        user = get_user_by_(verified_result["email"])
        try:
            return rpc_method(servicer_instance, request, context, user)
        except AccessDenied as error:
            context.abort(grpc.StatusCode.PERMISSION_DENIED, str(error))
            return

    return wrapper


def _get_token_from_(context_invocation_metadata: tuple) -> str | None:
    """Returns token from the given servicer context invocation metadata."""
    authorization_metadata = list(
        filter(
            lambda x: x.key == "authorization",
            context_invocation_metadata,
        )
    )[0]
    return authorization_metadata.value.split(" ")[1]  # Remove "Bearer "
