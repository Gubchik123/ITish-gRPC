from blog.protos import blog_pb2 as _blog_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserSchema(_message.Message):
    __slots__ = ["email", "username", "password"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    username: str
    password: str
    def __init__(self, email: _Optional[str] = ..., username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class UserDetailSchema(_message.Message):
    __slots__ = ["id", "email", "username", "created"]
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    id: int
    email: str
    username: str
    created: str
    def __init__(self, id: _Optional[int] = ..., email: _Optional[str] = ..., username: _Optional[str] = ..., created: _Optional[str] = ...) -> None: ...

class GetUserByUsernameRequest(_message.Message):
    __slots__ = ["username"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    username: str
    def __init__(self, username: _Optional[str] = ...) -> None: ...

class GetUserByUsernameResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: UserDetailSchema
    def __init__(self, user: _Optional[_Union[UserDetailSchema, _Mapping]] = ...) -> None: ...

class GetUserPostsRequest(_message.Message):
    __slots__ = ["username", "limit", "offset"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    username: str
    limit: int
    offset: int
    def __init__(self, username: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetUserPostsResponse(_message.Message):
    __slots__ = ["posts"]
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[_blog_pb2.PostListSchema]
    def __init__(self, posts: _Optional[_Iterable[_Union[_blog_pb2.PostListSchema, _Mapping]]] = ...) -> None: ...

class GetUserCommentsRequest(_message.Message):
    __slots__ = ["username", "limit", "offset"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    username: str
    limit: int
    offset: int
    def __init__(self, username: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetUserCommentsResponse(_message.Message):
    __slots__ = ["comments"]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[_blog_pb2.CommentSchema]
    def __init__(self, comments: _Optional[_Iterable[_Union[_blog_pb2.CommentSchema, _Mapping]]] = ...) -> None: ...

class GetUserLikedPostsRequest(_message.Message):
    __slots__ = ["username", "limit", "offset"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    username: str
    limit: int
    offset: int
    def __init__(self, username: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetUserLikedPostsResponse(_message.Message):
    __slots__ = ["posts"]
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[_blog_pb2.PostListSchema]
    def __init__(self, posts: _Optional[_Iterable[_Union[_blog_pb2.PostListSchema, _Mapping]]] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: UserSchema
    def __init__(self, user: _Optional[_Union[UserSchema, _Mapping]] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
