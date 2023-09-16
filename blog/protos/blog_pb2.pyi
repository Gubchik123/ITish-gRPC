from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostSchema(_message.Message):
    __slots__ = ["title", "body", "tags", "user_id"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    body: str
    tags: str
    user_id: int
    def __init__(self, title: _Optional[str] = ..., body: _Optional[str] = ..., tags: _Optional[str] = ..., user_id: _Optional[int] = ...) -> None: ...

class PostUpdateSchema(_message.Message):
    __slots__ = ["title", "body", "tags"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    title: str
    body: str
    tags: str
    def __init__(self, title: _Optional[str] = ..., body: _Optional[str] = ..., tags: _Optional[str] = ...) -> None: ...

class TagSchema(_message.Message):
    __slots__ = ["name", "slug"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    name: str
    slug: str
    def __init__(self, name: _Optional[str] = ..., slug: _Optional[str] = ...) -> None: ...

class CommentSchema(_message.Message):
    __slots__ = ["body", "post_id", "user_id"]
    BODY_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    body: str
    post_id: int
    user_id: int
    def __init__(self, body: _Optional[str] = ..., post_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class CommentUpdateSchema(_message.Message):
    __slots__ = ["id", "body"]
    ID_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    id: int
    body: str
    def __init__(self, id: _Optional[int] = ..., body: _Optional[str] = ...) -> None: ...

class LikeSchema(_message.Message):
    __slots__ = ["post_id", "user_id"]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    user_id: int
    def __init__(self, post_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class GetPostsRequest(_message.Message):
    __slots__ = ["limit", "offset"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetPostsResponse(_message.Message):
    __slots__ = ["posts"]
    POSTS_FIELD_NUMBER: _ClassVar[int]
    posts: _containers.RepeatedCompositeFieldContainer[PostSchema]
    def __init__(self, posts: _Optional[_Iterable[_Union[PostSchema, _Mapping]]] = ...) -> None: ...

class GetPostBySlugRequest(_message.Message):
    __slots__ = ["slug"]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class GetPostBySlugResponse(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: PostSchema
    def __init__(self, post: _Optional[_Union[PostSchema, _Mapping]] = ...) -> None: ...

class CreatePostRequest(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: PostSchema
    def __init__(self, post: _Optional[_Union[PostSchema, _Mapping]] = ...) -> None: ...

class CreatePostResponse(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: PostSchema
    def __init__(self, post: _Optional[_Union[PostSchema, _Mapping]] = ...) -> None: ...

class UpdatePostBySlugRequest(_message.Message):
    __slots__ = ["post", "post_slug"]
    POST_FIELD_NUMBER: _ClassVar[int]
    POST_SLUG_FIELD_NUMBER: _ClassVar[int]
    post: PostUpdateSchema
    post_slug: int
    def __init__(self, post: _Optional[_Union[PostUpdateSchema, _Mapping]] = ..., post_slug: _Optional[int] = ...) -> None: ...

class UpdatePostBySlugResponse(_message.Message):
    __slots__ = ["post"]
    POST_FIELD_NUMBER: _ClassVar[int]
    post: PostSchema
    def __init__(self, post: _Optional[_Union[PostSchema, _Mapping]] = ...) -> None: ...

class DeletePostBySlugRequest(_message.Message):
    __slots__ = ["slug"]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class DeletePostBySlugResponse(_message.Message):
    __slots__ = ["slug"]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class GetTagsRequest(_message.Message):
    __slots__ = ["limit", "offset"]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    limit: int
    offset: int
    def __init__(self, limit: _Optional[int] = ..., offset: _Optional[int] = ...) -> None: ...

class GetTagsResponse(_message.Message):
    __slots__ = ["tags"]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[TagSchema]
    def __init__(self, tags: _Optional[_Iterable[_Union[TagSchema, _Mapping]]] = ...) -> None: ...

class GetTagBySlugRequest(_message.Message):
    __slots__ = ["slug"]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    slug: str
    def __init__(self, slug: _Optional[str] = ...) -> None: ...

class GetTagBySlugResponse(_message.Message):
    __slots__ = ["tag", "posts"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    POSTS_FIELD_NUMBER: _ClassVar[int]
    tag: TagSchema
    posts: _containers.RepeatedCompositeFieldContainer[PostSchema]
    def __init__(self, tag: _Optional[_Union[TagSchema, _Mapping]] = ..., posts: _Optional[_Iterable[_Union[PostSchema, _Mapping]]] = ...) -> None: ...

class GetPostCommentsRequest(_message.Message):
    __slots__ = ["post_slug"]
    POST_SLUG_FIELD_NUMBER: _ClassVar[int]
    post_slug: str
    def __init__(self, post_slug: _Optional[str] = ...) -> None: ...

class GetPostCommentsResponse(_message.Message):
    __slots__ = ["comments"]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[CommentSchema]
    def __init__(self, comments: _Optional[_Iterable[_Union[CommentSchema, _Mapping]]] = ...) -> None: ...

class CreatePostCommentRequest(_message.Message):
    __slots__ = ["comment"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: CommentSchema
    def __init__(self, comment: _Optional[_Union[CommentSchema, _Mapping]] = ...) -> None: ...

class CreatePostCommentResponse(_message.Message):
    __slots__ = ["comment"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: CommentSchema
    def __init__(self, comment: _Optional[_Union[CommentSchema, _Mapping]] = ...) -> None: ...

class UpdatePostCommentRequest(_message.Message):
    __slots__ = ["comment"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: CommentUpdateSchema
    def __init__(self, comment: _Optional[_Union[CommentUpdateSchema, _Mapping]] = ...) -> None: ...

class UpdatePostCommentResponse(_message.Message):
    __slots__ = ["comment"]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: CommentSchema
    def __init__(self, comment: _Optional[_Union[CommentSchema, _Mapping]] = ...) -> None: ...

class DeletePostCommentRequest(_message.Message):
    __slots__ = ["comment_id"]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    def __init__(self, comment_id: _Optional[int] = ...) -> None: ...

class DeletePostCommentResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class GetPostLikesRequest(_message.Message):
    __slots__ = ["post_slug"]
    POST_SLUG_FIELD_NUMBER: _ClassVar[int]
    post_slug: str
    def __init__(self, post_slug: _Optional[str] = ...) -> None: ...

class GetPostLikesResponse(_message.Message):
    __slots__ = ["likes"]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    likes: _containers.RepeatedCompositeFieldContainer[LikeSchema]
    def __init__(self, likes: _Optional[_Iterable[_Union[LikeSchema, _Mapping]]] = ...) -> None: ...

class CreatePostLikeRequest(_message.Message):
    __slots__ = ["like"]
    LIKE_FIELD_NUMBER: _ClassVar[int]
    like: LikeSchema
    def __init__(self, like: _Optional[_Union[LikeSchema, _Mapping]] = ...) -> None: ...

class CreatePostLikeResponse(_message.Message):
    __slots__ = ["like"]
    LIKE_FIELD_NUMBER: _ClassVar[int]
    like: LikeSchema
    def __init__(self, like: _Optional[_Union[LikeSchema, _Mapping]] = ...) -> None: ...

class DeletePostLikeRequest(_message.Message):
    __slots__ = ["like_id"]
    LIKE_ID_FIELD_NUMBER: _ClassVar[int]
    like_id: int
    def __init__(self, like_id: _Optional[int] = ...) -> None: ...

class DeletePostLikeResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
