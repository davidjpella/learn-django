import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Post

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        filter_fields = {
            'id': ['exact'],
            'title': ['exact', 'icontains', 'istartswith'],
            'created_at': ['gt', 'lt', 'gte', 'lte'],
            'updated_at': ['gt', 'lt', 'gte', 'lte'],
        }
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):
    post = relay.Node.Field(PostType)
    posts = DjangoFilterConnectionField(PostType)

schema = graphene.Schema(query=Query)
