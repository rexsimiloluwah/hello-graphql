import graphene
from flask import Flask
from config import Config
from flask_graphql import GraphQLView
from app.api.schema import (
    Query,
    Mutation
)
from app.models import Base,engine,db_session
Base.metadata.create_all(engine)

# Database engine 

schema = graphene.Schema(query=Query, mutation=Mutation)

def init_app():
    app = Flask(__name__)

    # Load app configuration 
    app.config.from_object(get_app_config())
    
    @app.teardown_appcontext 
    def shutdown_session(exception=None)->None:
        db_session.remove()

    @app.route("/")
    def hello() -> str:
        return "Hello World, We are under construction."
    
    app.add_url_rule(
       '/graphql',
        view_func=GraphQLView.as_view(
           'graphql',
           schema=schema,
           graphiql=True
       )
    )
    return app

def get_app_config():
    if Config.ENV == "development":
        return "config.DevelopmentConfig" 
    if Config.ENV == "testing":
        return "config.TestingConfig" 
    if Config.ENV == "production":
        return "config.ProductionConfig"