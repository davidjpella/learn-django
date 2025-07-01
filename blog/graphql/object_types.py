import graphene
from graphene import relay
from graphene_django import DjangoObjectType, DjangoListField
from ..models import Post, Author, Comment


class AuthorType(DjangoObjectType):
    posts_count = graphene.Int()

    class Meta:
        model = Author
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)

    def __init__(self):
        self.posts = None

    def resolve_posts_count(self, info):
        return getattr(self, "posts_count", self.posts.count())


class PostType(DjangoObjectType):
    comments = DjangoListField(lambda: CommentType)

    class Meta:
        model = Post
        filter_fields = {
            'id': ['exact'],
            'title': ['exact', 'icontains', 'istartswith'],
            'created_at': ['gt', 'lt', 'gte', 'lte'],
            'updated_at': ['gt', 'lt', 'gte', 'lte'],
        }
        interfaces = (relay.Node,)

    # def resolve_author(self, info):
    #     return self.author
    #
    # def resolve_comments(self, info):
    #     return self.comments


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        filter_fields = {
            'id': ['exact'],
            'content': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)
