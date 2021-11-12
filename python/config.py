import os 
from decouple import config

ENV = config("ENV")
DB_USERNAME = config("DB_USERNAME")
DB_PASSWORD = config("DB_PASSWORD")
DB_PORT = config("DB_PORT", default=5432)
DB_HOST = config("DB_HOST")
DB_NAME = config("DB_NAME")
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class Config:
    ENV = ENV
    CSRF_ENABLED = True 
    SECRET_KEY = "algorhythm" 
    JWT_SECRET_KEY = config("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = int(config("JWT_ACCESS_TOKEN_EXPIRES")) # In minutes
    JWT_REFRESH_TOKEN_EXPIRES = int(config("JWT_REFRESH_TOKEN_EXPIRES"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True 

class TestingConfig(Config):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = True
