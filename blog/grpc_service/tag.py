import logging

import grpc
from sqlalchemy.orm.exc import NoResultFound

import models
from decorators import catch_not_found_

from .. import crud
from ..protos import blog_pb2
from ..protos import blog_pb2_grpc


logger = logging.getLogger(__name__)


class TagBlogServicer(blog_pb2_grpc.BlogServicer):
    """Servicer to provide tag methods that implements blog server."""

    def GetTags(
        self, request: blog_pb2.GetTagsRequest, context: grpc.ServicerContext
    ) -> blog_pb2.GetTagsResponse:
        """Returns a list of tags."""
        logger.info("GetTags")
        tags = crud.get_all_tags(request.limit, request.offset)
        return blog_pb2.GetTagsResponse(
            tags=(self._get_tag_schema_from_(tag) for tag in tags)
        )

    @catch_not_found_("Tag")
    def GetTagBySlug(
        self,
        request: blog_pb2.GetTagBySlugRequest,
        context: grpc.ServicerContext,
    ) -> blog_pb2.GetTagBySlugResponse:
        """Returns a tag by slug."""
        logger.info("GetTagBySlug")
        tag = crud.get_tag_by_slug(request.slug)
        return blog_pb2.GetTagBySlugResponse(
            tag=self._get_tag_schema_from_(tag),
            posts=(
                self._get_post_list_schema_from_(post) for post in tag.posts
            ),
        )

    def _get_tag_schema_from_(self, tag: models.Tag) -> blog_pb2.TagSchema:
        """Returns a TagSchema from the given Tag model."""
        return blog_pb2.TagSchema(
            title=tag.title,
            slug=tag.slug,
        )