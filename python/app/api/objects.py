import graphene 
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import User as UserModel,Post as PostModel,Comment as CommentModel 

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel 

class Post(SQLAlchemyObjectType):
    class Meta:
        model = PostModel 

class Comment(SQLAlchemyObjectType):
    class Meta:
        model = CommentModel 
