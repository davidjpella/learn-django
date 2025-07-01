import graphene
from .object_types import AuthorType
from ..models import Author


class CreateAuthorMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, name):
        author = Author.objects.create(name=name)
        return CreateAuthorMutation(author=author)


class UpdateAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, id, name):
        try:
            author = Author.objects.get(pk=id)
            author.name = name
            author.save()
            return UpdateAuthorMutation(author=author)
        except Author.DoesNotExist:
            raise Exception("Author not found.")


class DeleteAuthorMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        try:
            author = Author.objects.get(pk=id)
            author.delete()
            return DeleteAuthorMutation(success=True)
        except Author.DoesNotExist:
            raise Exception("Author not found.")


class Mutation(graphene.ObjectType):
    create_author = CreateAuthorMutation.Field()
    update_author = UpdateAuthorMutation.Field()
    delete_author = DeleteAuthorMutation.Field()
