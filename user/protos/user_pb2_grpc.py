# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from blog.protos import blog_pb2 as blog_dot_protos_dot_blog__pb2
from user.protos import user_pb2 as user_dot_protos_dot_user__pb2


class UserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetUserByUsername = channel.unary_unary(
                '/user.User/GetUserByUsername',
                request_serializer=user_dot_protos_dot_user__pb2.GetUserByUsernameRequest.SerializeToString,
                response_deserializer=user_dot_protos_dot_user__pb2.GetUserByUsernameResponse.FromString,
                )
        self.GetUserPosts = channel.unary_unary(
                '/user.User/GetUserPosts',
                request_serializer=user_dot_protos_dot_user__pb2.GetUserPostsRequest.SerializeToString,
                response_deserializer=user_dot_protos_dot_user__pb2.GetUserPostsResponse.FromString,
                )
        self.GetUserComments = channel.unary_unary(
                '/user.User/GetUserComments',
                request_serializer=user_dot_protos_dot_user__pb2.GetUserCommentsRequest.SerializeToString,
                response_deserializer=user_dot_protos_dot_user__pb2.GetUserCommentsResponse.FromString,
                )
        self.GetUserLikedPosts = channel.unary_unary(
                '/user.User/GetUserLikedPosts',
                request_serializer=user_dot_protos_dot_user__pb2.GetUserLikedPostsRequest.SerializeToString,
                response_deserializer=user_dot_protos_dot_user__pb2.GetUserLikedPostsResponse.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/user.User/UpdateUser',
                request_serializer=user_dot_protos_dot_user__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=blog_dot_protos_dot_blog__pb2.StatusResponse.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/user.User/DeleteUser',
                request_serializer=user_dot_protos_dot_user__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=blog_dot_protos_dot_blog__pb2.StatusResponse.FromString,
                )


class UserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetUserByUsername(self, request, context):
        """Getting methods --------------------------------------------------------------------
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserPosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserComments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserLikedPosts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Processing methods -----------------------------------------------------------------
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetUserByUsername': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByUsername,
                    request_deserializer=user_dot_protos_dot_user__pb2.GetUserByUsernameRequest.FromString,
                    response_serializer=user_dot_protos_dot_user__pb2.GetUserByUsernameResponse.SerializeToString,
            ),
            'GetUserPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserPosts,
                    request_deserializer=user_dot_protos_dot_user__pb2.GetUserPostsRequest.FromString,
                    response_serializer=user_dot_protos_dot_user__pb2.GetUserPostsResponse.SerializeToString,
            ),
            'GetUserComments': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserComments,
                    request_deserializer=user_dot_protos_dot_user__pb2.GetUserCommentsRequest.FromString,
                    response_serializer=user_dot_protos_dot_user__pb2.GetUserCommentsResponse.SerializeToString,
            ),
            'GetUserLikedPosts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserLikedPosts,
                    request_deserializer=user_dot_protos_dot_user__pb2.GetUserLikedPostsRequest.FromString,
                    response_serializer=user_dot_protos_dot_user__pb2.GetUserLikedPostsResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=user_dot_protos_dot_user__pb2.UpdateUserRequest.FromString,
                    response_serializer=blog_dot_protos_dot_blog__pb2.StatusResponse.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=user_dot_protos_dot_user__pb2.DeleteUserRequest.FromString,
                    response_serializer=blog_dot_protos_dot_blog__pb2.StatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user.User', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class User(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetUserByUsername(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetUserByUsername',
            user_dot_protos_dot_user__pb2.GetUserByUsernameRequest.SerializeToString,
            user_dot_protos_dot_user__pb2.GetUserByUsernameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetUserPosts',
            user_dot_protos_dot_user__pb2.GetUserPostsRequest.SerializeToString,
            user_dot_protos_dot_user__pb2.GetUserPostsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserComments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetUserComments',
            user_dot_protos_dot_user__pb2.GetUserCommentsRequest.SerializeToString,
            user_dot_protos_dot_user__pb2.GetUserCommentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserLikedPosts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/GetUserLikedPosts',
            user_dot_protos_dot_user__pb2.GetUserLikedPostsRequest.SerializeToString,
            user_dot_protos_dot_user__pb2.GetUserLikedPostsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/UpdateUser',
            user_dot_protos_dot_user__pb2.UpdateUserRequest.SerializeToString,
            blog_dot_protos_dot_blog__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user.User/DeleteUser',
            user_dot_protos_dot_user__pb2.DeleteUserRequest.SerializeToString,
            blog_dot_protos_dot_blog__pb2.StatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
