"""graphQL schemas."""

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db, User

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserObject)

schema = graphene.Schema(query=Query)

class AddUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, username, email):
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return AddUser(user=user)

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
