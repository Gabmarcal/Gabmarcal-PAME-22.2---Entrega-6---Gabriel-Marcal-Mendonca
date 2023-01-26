from os import environ
from dotenv import load_dotenv

load_dotenv
class Config:
    SQLALCHEMY_DATABASE_URI = environ.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.SQLALCHEMY_TRACK_MODIFICATIONS
    JWT_SECRET_KEYS = environ.JWT_SECRET_KEYS