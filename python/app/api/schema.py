import graphene 
from graphene import relay  
from graphene_sqlalchemy import SQLAlchemyConnectionField 
from app.models import db_session 
from app.models import (
    User as UserModel,
    Post as PostModel,
    Comment as CommentModel,
)
from app.api.objects import (
    User as UserObject,
    Post as PostObject,
    Comment as CommentObject,
) 

class Query(graphene.ObjectType):
    users = graphene.List(lambda:UserObject)
    posts = graphene.List(lambda:PostObject)
    user = graphene.Field(UserObject, id=graphene.Int())
    user_by_name = graphene.Field(UserObject, username=graphene.String())
    post = graphene.Field(PostObject, id=graphene.Int())
    posts_by_category = graphene.List(lambda:PostObject, category=graphene.String())
    comments = graphene.List(lambda:CommentObject, post_id=graphene.Int())

    def resolve_users(self,info):
        return UserModel.query.all()

    def resolve_posts(self,info):
        return PostModel.query.all()

    def resolve_user(self,info,id):
        return UserModel.query.filter_by(id=id).first()

    def resolve_user_by_name(self,info,username):
        return UserModel.query.filter_by(username=username).first()

    def resolve_comments(self,info,post_id):
        return CommentModel.query.filter_by(post_id=post_id).all()

    def resolve_post(self,info,id):
        return PostModel.query.filter_by(id=id).first()

    def resolve_posts_by_category(self,info,category):
        return PostModel.query.filter_by(category=category).all() 

class CreateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=False)
        name = graphene.String(required=True)
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        phone = graphene.String(required=False)
        website = graphene.String(required=False)
        bio = graphene.String(required=False)

    user = graphene.Field(lambda:UserObject)

    def mutate(self,info,name,username,email,password,bio,phone=None,website=None):
        user = UserModel.query.filter_by(email=email).first()
        if user:
            return CreateUser(
                    user=user
                )
        user = UserModel(
            name=name,
            username=username, 
            email=email,
            password=password,
            phone=phone,
            website=website,
            bio=bio
        )
        db_session.add(user)
        db_session.commit()
        return CreateUser(
            user=user
        )
class AddPost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=False)
        title = graphene.String(required=True)
        category = graphene.String(required=True)
        content = graphene.String(required=True)
        tags = graphene.List(graphene.String)
        user_id = graphene.Int(required=True)

    post = graphene.Field(lambda:PostObject)

    def mutate(self,info,title,category,content,tags,user_id):
        post = PostModel(
            title=title,
            category=category,
            content=content,
            tags=tags,
            user_id=user_id
        )
        db_session.add(post)
        db_session.commit()
        return AddPost(
            post=post
        )

class AddComment(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=False)
        comment = graphene.String(required=True)
        post_id = graphene.Int(required=True)
        user_id = graphene.Int(required=True)

    comment = graphene.Field(lambda:CommentObject)
    def mutate(self,info,comment,post_id,user_id):
        comment = CommentModel(
            comment=comment,
            post_id=post_id,
            user_id=user_id,
        )
        db_session.add(comment)
        db_session.commit()
        return AddComment(
            comment=comment
        )

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    add_post = AddPost.Field()
    add_comment = AddComment.Field()