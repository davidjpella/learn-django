import django_filters
import graphene
from graphene import relay
from django_filters import FilterSet, OrderingFilter
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

class PostFilter(FilterSet):
    title = django_filters.CharFilter(
        lookup_expr=['iexact', 'icontains', 'istartswith']
    )
    content = django_filters.CharFilter(
        lookup_expr=['iexact', 'icontains', 'istartswith']
    )
    created_at = django_filters.DateFilter(
        lookup_expr=['gt', 'lt', 'gte', 'lte']
    )
    updated_at = django_filters.DateFilter(
        lookup_expr=['gt', 'lt', 'gte', 'lte']
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']

    order_by = OrderingFilter(
        fields=(
            ('id', 'created_at'),
        )
    )


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        filterset_class = PostFilter
        interfaces = (relay.Node,)

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        filter_fields = {
            'id': ['exact'],
            'content': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)
