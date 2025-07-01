import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from .object_types import AuthorType, PostType, CommentType
from ..models import Post


class Query(graphene.ObjectType):
    author = relay.Node.Field(AuthorType)
    authors = DjangoFilterConnectionField(AuthorType)

    post = relay.Node.Field(PostType)
    posts = DjangoFilterConnectionField(PostType)

    comment = relay.Node.Field(CommentType)
    comments = DjangoFilterConnectionField(CommentType)

    all_posts = graphene.List(PostType)

    def resolve_all_posts(root, info):
        return Post.objects.select_related('author').all()
