import graphene 
from graphene import relay  
import inspect
from app.models import db_session 
from flask_bcrypt import check_password_hash
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
from flask_graphql_auth import (
    AuthInfoField,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    mutation_jwt_refresh_token_required,
    query_header_jwt_required,
    mutation_header_jwt_required,
)

# Authenticated route (https://flask-graphql-auth.readthedocs.io/en/latest/basic_usage.html)
# For protected queries and mutations, we need to make a union between the object and the AuthInfoField
# This enables the auth decorators to return the AuthInfoField when an authentication is valid or invalid
class ProtectedUser(graphene.Union):
    class Meta:
        types = (UserObject,AuthInfoField)

class ProtectedPost(graphene.Union):
    class Meta:
        types = (PostObject,AuthInfoField)

class ProtectedComment(graphene.Union):
    class Meta:
        types = (CommentObject,AuthInfoField)

class ProtectedRefreshToken(graphene.Union):
    class Meta:
        types = (graphene.String(),AuthInfoField)

class Query(graphene.ObjectType):
    get_users = graphene.List(lambda:UserObject)
    get_posts = graphene.List(lambda:PostObject)
    get_user = graphene.Field(type=ProtectedUser, id=graphene.Int())
    get_user_by_name = graphene.Field(UserObject, username=graphene.String())
    get_post = graphene.Field(PostObject, id=graphene.Int())
    get_posts_by_category = graphene.List(lambda:PostObject, category=graphene.String())
    get_comments = graphene.List(lambda:CommentObject, post_id=graphene.Int())
    get_user_posts = graphene.List(lambda:PostObject, user_id=graphene.Int())
    get_post_comments = graphene.List(lambda:CommentObject, post_id=graphene.Int())

    def resolve_get_users(self,info):
        return UserModel.query.all()

    def resolve_get_posts(self,info):
        return PostModel.query.all()

    def resolve_get_user_by_name(self,info,username:str):
        user = UserModel.query.filter_by(username=username).first()
        return user

    def resolve_get_comments(self,info,post_id:int):
        return CommentModel.query.filter_by(post_id=post_id).all()

    def resolve_get_post(self,info,id:int):
        return PostModel.query.filter_by(id=id).first()

    def resolve_get_posts_by_category(self,info,category:str):
        return PostModel.query.filter_by(category=category).all() 

    def resolve_get_user_posts(self,info,user_id:int):
        return PostModel.query.filter_by(user_id=user_id).all()

    def resolve_get_post_comments(self,info,post_id:int):
        return CommentModel.query.filter_by(post_id=post_id).all()

    # Testing the query_header_jwt_required decorator for protected query routes
    @query_header_jwt_required
    def resolve_get_user(self,info,id):
        return UserModel.query.filter_by(id=id).first()

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

    def mutate(self,info,name:str,username:str,email:str,password:str,bio:str,phone:str=None,website:str=None):
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
        user.set_password(password)
        db_session.add(user)
        db_session.commit()
        return CreateUser(
            user=user
        )

class AuthMutation(graphene.Mutation):
    access_token = graphene.String()
    refresh_token = graphene.String()
    user = graphene.Field(lambda:UserObject)

    class Arguments:
        email = graphene.String()
        password = graphene.String()
        
    def mutate(self,info,email:str,password:str):
        user = UserModel.query.filter_by(email=email).first()
        print(user)
        if not user:
            raise Exception("Authorization Failed, User does not exist.")
        if not user.check_password(password):
            raise Exception("Authorization Failed, Password is Incorrect.")
        return AuthMutation(
            user=user,
            access_token=create_access_token(identity={
                'id': user.id,
                'email': user.email
            }),
            refresh_token=create_refresh_token(identity={
                'id': user.id,
                'email': user.email
            })
        )

class AddPost(graphene.Mutation):
    post = graphene.Field(type=ProtectedPost)

    class Arguments(object):
        id = graphene.Int(required=False)
        title = graphene.String(required=True)
        category = graphene.String(required=True)
        content = graphene.String(required=True)
        tags = graphene.List(graphene.String)

    @classmethod
    @mutation_header_jwt_required
    def mutate(self,_,info,title:str,category:str,content:str,tags:list=None):
        current_user = get_jwt_identity()
        print('Current user:',current_user)
        if current_user:
            user_id = current_user['id']
        post = PostModel(
            title=title,
            category=category,
            content=content,
            tags=",".join(tags),
            user_id=user_id
        )
        db_session.add(post)
        db_session.commit()
        return AddPost(
            post=post
        )

class UpdatePost(graphene.Mutation):
    post = graphene.Field(ProtectedPost)

    class Arguments(object):
        id = graphene.Int(required=True)
        title = graphene.String()
        content = graphene.String()
        category = graphene.String()
        tags = graphene.List(graphene.String)

    @classmethod 
    @mutation_header_jwt_required 
    def mutate(self,_,info,id:int,title:str=None,content:str=None,category:str=None,tags:list=None):
        post = PostModel.query.filter_by(id=id).first()
        if not post:
            raise Exception("Post not found")
        if title is not None:
            post.title = title 
        if content is not None:
            post.content = content 
        if category is not None:
            post.category = category 
        if tags is not None:
            post.tags = ",".join(tags) 
        db_session.commit()
        return UpdatePost(
            post=post
        )

class DeletePost(graphene.Mutation):
    post = graphene.Field(ProtectedPost) 

    class Arguments(object):
        id = graphene.Int(required=True)

    @classmethod 
    @mutation_header_jwt_required
    def mutate(self,_,info,id:int):
        current_user = get_jwt_identity()
        if not current_user:
            raise Exception("Authentication required.")
        post = PostModel.query.filter_by(id=id).first()
        if post.user_id != current_user['id']:
            raise Exception("This user cannot delete this post.")
        db_session.delete(post)
        db_session.commit()
        return DeletePost(
            post=post
        )
        
class AddComment(graphene.Mutation):
    comment = graphene.Field(type=ProtectedComment)

    class Arguments(object):
        id = graphene.Int(required=False)
        content = graphene.String(required=True)
        post_id = graphene.Int(required=True)

    @classmethod 
    @mutation_header_jwt_required
    def mutate(self,_,info,content:str,post_id:int):
        current_user = get_jwt_identity()
        if not current_user:
            raise Exception('Authentication is required.')
        post = PostModel.query.filter_by(id=post_id).first()
        print(post)
        if not post:
            raise Exception("Post not found")
        user_id = current_user['id']
        comment = CommentModel(
            comment=content,
            post_id=post_id,
            user_id=user_id,
        )
        db_session.add(comment)
        db_session.commit()
        return AddComment(
            comment=comment
        )

class UpdateComment(graphene.Mutation):
    comment = graphene.Field(type=ProtectedComment)

    class Arguments(object):
        id = graphene.Int(required=True)
        content = graphene.String()

    @classmethod 
    @mutation_header_jwt_required
    def mutate(self,_,info,id:int,content:str=None):
        current_user = get_jwt_identity()
        if not current_user:
            raise Exception('Authentication is required.')
        
        comment = CommentModel.query.filter_by(id=id).first()
        if not comment:
            raise Exception('Comment not found.')
        comment.comment = content
        db_session.commit()
        return UpdateComment(
            comment=comment
        )         

class DeleteComment(graphene.Mutation):
    comment = graphene.Field(type=ProtectedComment)

    class Arguments(object):
        id = graphene.Int(required=True)

    @classmethod 
    @mutation_header_jwt_required
    def mutate(self,_,info,id:int):
        current_user = get_jwt_identity()
        if not current_user:
            raise Exception('Authentication is required.')
        comment = CommentModel.query.filter_by(id=id).first()
        if not comment:
            raise Exception('Comment not found.')
        print(comment)
        if comment.user_id != current_user['id']:
            raise Exception('This user is not authorized to delete this comment.')
        db_session.delete(comment)
        db_session.commit()
        return DeleteComment(
            comment=comment
        )

class RefreshMutation(graphene.Mutation):
    class Arguments:
        refresh_token = graphene.String()

    user = graphene.Field(lambda:UserObject)
    access_token = graphene.String()

    @mutation_jwt_refresh_token_required
    def mutate(self):
        current_user = get_jwt_identity()
        user = UserModel.query.filter_by(id=current_user['id']).first()
        return RefreshMutation(
            user=user,
            access_token=create_access_token(identity={
                'id':current_user['id'],
                'email':current_user['email']
            })
        )
    
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    add_post = AddPost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
    add_comment = AddComment.Field()
    update_comment = UpdateComment.Field()
    delete_comment = DeleteComment.Field()
    login_user = AuthMutation.Field()
    refresh_token = RefreshMutation.Field()