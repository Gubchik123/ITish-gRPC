# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blog/protos/blog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x62log/protos/blog.proto\x12\x04\x62log\"H\n\nPostSchema\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x04 \x01(\x03\"=\n\x10PostUpdateSchema\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\x0c\n\x04tags\x18\x03 \x01(\t\"\'\n\tTagSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04slug\x18\x02 \x01(\t\"P\n\rCommentSchema\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\x12\x0f\n\x07post_id\x18\x02 \x01(\x03\x12\x14\n\x07user_id\x18\x03 \x01(\x03H\x00\x88\x01\x01\x42\n\n\x08_user_id\"/\n\x13\x43ommentUpdateSchema\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\"?\n\nLikeSchema\x12\x0f\n\x07post_id\x18\x01 \x01(\x03\x12\x14\n\x07user_id\x18\x02 \x01(\x03H\x00\x88\x01\x01\x42\n\n\x08_user_id\"0\n\x0fGetPostsRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\"3\n\x10GetPostsResponse\x12\x1f\n\x05posts\x18\x01 \x03(\x0b\x32\x10.blog.PostSchema\"$\n\x14GetPostBySlugRequest\x12\x0c\n\x04slug\x18\x01 \x01(\t\"7\n\x15GetPostBySlugResponse\x12\x1e\n\x04post\x18\x01 \x01(\x0b\x32\x10.blog.PostSchema\"3\n\x11\x43reatePostRequest\x12\x1e\n\x04post\x18\x01 \x01(\x0b\x32\x10.blog.PostSchema\"4\n\x12\x43reatePostResponse\x12\x1e\n\x04post\x18\x01 \x01(\x0b\x32\x10.blog.PostSchema\"R\n\x17UpdatePostBySlugRequest\x12$\n\x04post\x18\x01 \x01(\x0b\x32\x16.blog.PostUpdateSchema\x12\x11\n\tpost_slug\x18\x02 \x01(\x03\":\n\x18UpdatePostBySlugResponse\x12\x1e\n\x04post\x18\x01 \x01(\x0b\x32\x10.blog.PostSchema\"\'\n\x17\x44\x65letePostBySlugRequest\x12\x0c\n\x04slug\x18\x01 \x01(\t\"(\n\x18\x44\x65letePostBySlugResponse\x12\x0c\n\x04slug\x18\x01 \x01(\t\"/\n\x0eGetTagsRequest\x12\r\n\x05limit\x18\x01 \x01(\x03\x12\x0e\n\x06offset\x18\x02 \x01(\x03\"0\n\x0fGetTagsResponse\x12\x1d\n\x04tags\x18\x01 \x03(\x0b\x32\x0f.blog.TagSchema\"#\n\x13GetTagBySlugRequest\x12\x0c\n\x04slug\x18\x01 \x01(\t\"U\n\x14GetTagBySlugResponse\x12\x1c\n\x03tag\x18\x01 \x01(\x0b\x32\x0f.blog.TagSchema\x12\x1f\n\x05posts\x18\x02 \x03(\x0b\x32\x10.blog.PostSchema\"+\n\x16GetPostCommentsRequest\x12\x11\n\tpost_slug\x18\x01 \x01(\t\"@\n\x17GetPostCommentsResponse\x12%\n\x08\x63omments\x18\x01 \x03(\x0b\x32\x13.blog.CommentSchema\"@\n\x18\x43reatePostCommentRequest\x12$\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x13.blog.CommentSchema\"A\n\x19\x43reatePostCommentResponse\x12$\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x13.blog.CommentSchema\"F\n\x18UpdatePostCommentRequest\x12*\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x19.blog.CommentUpdateSchema\"A\n\x19UpdatePostCommentResponse\x12$\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x13.blog.CommentSchema\".\n\x18\x44\x65letePostCommentRequest\x12\x12\n\ncomment_id\x18\x01 \x01(\x03\"+\n\x19\x44\x65letePostCommentResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"(\n\x13GetPostLikesRequest\x12\x11\n\tpost_slug\x18\x01 \x01(\t\"7\n\x14GetPostLikesResponse\x12\x1f\n\x05likes\x18\x01 \x03(\x0b\x32\x10.blog.LikeSchema\"7\n\x15\x43reatePostLikeRequest\x12\x1e\n\x04like\x18\x01 \x01(\x0b\x32\x10.blog.LikeSchema\"8\n\x16\x43reatePostLikeResponse\x12\x1e\n\x04like\x18\x01 \x01(\x0b\x32\x10.blog.LikeSchema\"(\n\x15\x44\x65letePostLikeRequest\x12\x0f\n\x07like_id\x18\x01 \x01(\x03\"(\n\x16\x44\x65letePostLikeResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2\xc0\x08\n\x04\x42log\x12;\n\x08GetPosts\x12\x15.blog.GetPostsRequest\x1a\x16.blog.GetPostsResponse\"\x00\x12J\n\rGetPostBySlug\x12\x1a.blog.GetPostBySlugRequest\x1a\x1b.blog.GetPostBySlugResponse\"\x00\x12\x41\n\nCreatePost\x12\x17.blog.CreatePostRequest\x1a\x18.blog.CreatePostResponse\"\x00\x12S\n\x10UpdatePostBySlug\x12\x1d.blog.UpdatePostBySlugRequest\x1a\x1e.blog.UpdatePostBySlugResponse\"\x00\x12S\n\x10\x44\x65letePostBySlug\x12\x1d.blog.DeletePostBySlugRequest\x1a\x1e.blog.DeletePostBySlugResponse\"\x00\x12\x38\n\x07GetTags\x12\x14.blog.GetTagsRequest\x1a\x15.blog.GetTagsResponse\"\x00\x12G\n\x0cGetTagBySlug\x12\x19.blog.GetTagBySlugRequest\x1a\x1a.blog.GetTagBySlugResponse\"\x00\x12P\n\x0fGetPostComments\x12\x1c.blog.GetPostCommentsRequest\x1a\x1d.blog.GetPostCommentsResponse\"\x00\x12V\n\x11\x43reatePostComment\x12\x1e.blog.CreatePostCommentRequest\x1a\x1f.blog.CreatePostCommentResponse\"\x00\x12V\n\x11UpdatePostComment\x12\x1e.blog.UpdatePostCommentRequest\x1a\x1f.blog.UpdatePostCommentResponse\"\x00\x12V\n\x11\x44\x65letePostComment\x12\x1e.blog.DeletePostCommentRequest\x1a\x1f.blog.DeletePostCommentResponse\"\x00\x12G\n\x0cGetPostLikes\x12\x19.blog.GetPostLikesRequest\x1a\x1a.blog.GetPostLikesResponse\"\x00\x12M\n\x0e\x43reatePostLike\x12\x1b.blog.CreatePostLikeRequest\x1a\x1c.blog.CreatePostLikeResponse\"\x00\x12M\n\x0e\x44\x65letePostLike\x12\x1b.blog.DeletePostLikeRequest\x1a\x1c.blog.DeletePostLikeResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'blog.protos.blog_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_POSTSCHEMA']._serialized_start=32
  _globals['_POSTSCHEMA']._serialized_end=104
  _globals['_POSTUPDATESCHEMA']._serialized_start=106
  _globals['_POSTUPDATESCHEMA']._serialized_end=167
  _globals['_TAGSCHEMA']._serialized_start=169
  _globals['_TAGSCHEMA']._serialized_end=208
  _globals['_COMMENTSCHEMA']._serialized_start=210
  _globals['_COMMENTSCHEMA']._serialized_end=290
  _globals['_COMMENTUPDATESCHEMA']._serialized_start=292
  _globals['_COMMENTUPDATESCHEMA']._serialized_end=339
  _globals['_LIKESCHEMA']._serialized_start=341
  _globals['_LIKESCHEMA']._serialized_end=404
  _globals['_GETPOSTSREQUEST']._serialized_start=406
  _globals['_GETPOSTSREQUEST']._serialized_end=454
  _globals['_GETPOSTSRESPONSE']._serialized_start=456
  _globals['_GETPOSTSRESPONSE']._serialized_end=507
  _globals['_GETPOSTBYSLUGREQUEST']._serialized_start=509
  _globals['_GETPOSTBYSLUGREQUEST']._serialized_end=545
  _globals['_GETPOSTBYSLUGRESPONSE']._serialized_start=547
  _globals['_GETPOSTBYSLUGRESPONSE']._serialized_end=602
  _globals['_CREATEPOSTREQUEST']._serialized_start=604
  _globals['_CREATEPOSTREQUEST']._serialized_end=655
  _globals['_CREATEPOSTRESPONSE']._serialized_start=657
  _globals['_CREATEPOSTRESPONSE']._serialized_end=709
  _globals['_UPDATEPOSTBYSLUGREQUEST']._serialized_start=711
  _globals['_UPDATEPOSTBYSLUGREQUEST']._serialized_end=793
  _globals['_UPDATEPOSTBYSLUGRESPONSE']._serialized_start=795
  _globals['_UPDATEPOSTBYSLUGRESPONSE']._serialized_end=853
  _globals['_DELETEPOSTBYSLUGREQUEST']._serialized_start=855
  _globals['_DELETEPOSTBYSLUGREQUEST']._serialized_end=894
  _globals['_DELETEPOSTBYSLUGRESPONSE']._serialized_start=896
  _globals['_DELETEPOSTBYSLUGRESPONSE']._serialized_end=936
  _globals['_GETTAGSREQUEST']._serialized_start=938
  _globals['_GETTAGSREQUEST']._serialized_end=985
  _globals['_GETTAGSRESPONSE']._serialized_start=987
  _globals['_GETTAGSRESPONSE']._serialized_end=1035
  _globals['_GETTAGBYSLUGREQUEST']._serialized_start=1037
  _globals['_GETTAGBYSLUGREQUEST']._serialized_end=1072
  _globals['_GETTAGBYSLUGRESPONSE']._serialized_start=1074
  _globals['_GETTAGBYSLUGRESPONSE']._serialized_end=1159
  _globals['_GETPOSTCOMMENTSREQUEST']._serialized_start=1161
  _globals['_GETPOSTCOMMENTSREQUEST']._serialized_end=1204
  _globals['_GETPOSTCOMMENTSRESPONSE']._serialized_start=1206
  _globals['_GETPOSTCOMMENTSRESPONSE']._serialized_end=1270
  _globals['_CREATEPOSTCOMMENTREQUEST']._serialized_start=1272
  _globals['_CREATEPOSTCOMMENTREQUEST']._serialized_end=1336
  _globals['_CREATEPOSTCOMMENTRESPONSE']._serialized_start=1338
  _globals['_CREATEPOSTCOMMENTRESPONSE']._serialized_end=1403
  _globals['_UPDATEPOSTCOMMENTREQUEST']._serialized_start=1405
  _globals['_UPDATEPOSTCOMMENTREQUEST']._serialized_end=1475
  _globals['_UPDATEPOSTCOMMENTRESPONSE']._serialized_start=1477
  _globals['_UPDATEPOSTCOMMENTRESPONSE']._serialized_end=1542
  _globals['_DELETEPOSTCOMMENTREQUEST']._serialized_start=1544
  _globals['_DELETEPOSTCOMMENTREQUEST']._serialized_end=1590
  _globals['_DELETEPOSTCOMMENTRESPONSE']._serialized_start=1592
  _globals['_DELETEPOSTCOMMENTRESPONSE']._serialized_end=1635
  _globals['_GETPOSTLIKESREQUEST']._serialized_start=1637
  _globals['_GETPOSTLIKESREQUEST']._serialized_end=1677
  _globals['_GETPOSTLIKESRESPONSE']._serialized_start=1679
  _globals['_GETPOSTLIKESRESPONSE']._serialized_end=1734
  _globals['_CREATEPOSTLIKEREQUEST']._serialized_start=1736
  _globals['_CREATEPOSTLIKEREQUEST']._serialized_end=1791
  _globals['_CREATEPOSTLIKERESPONSE']._serialized_start=1793
  _globals['_CREATEPOSTLIKERESPONSE']._serialized_end=1849
  _globals['_DELETEPOSTLIKEREQUEST']._serialized_start=1851
  _globals['_DELETEPOSTLIKEREQUEST']._serialized_end=1891
  _globals['_DELETEPOSTLIKERESPONSE']._serialized_start=1893
  _globals['_DELETEPOSTLIKERESPONSE']._serialized_end=1933
  _globals['_BLOG']._serialized_start=1936
  _globals['_BLOG']._serialized_end=3024
# @@protoc_insertion_point(module_scope)
