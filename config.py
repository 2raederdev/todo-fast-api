from os import environ
from dotenv import load_dotenv

USE_DOTENV = environ.get("USE_DOTENV")

if(USE_DOTENV):
    load_dotenv()

config = {
    'ENV': environ.get('ENV') or 'development',
    'SECRET_KEY': environ.get('SECRET_KEY') or 'secret',
    'PORT': environ.get('PORT') or 8000,
    'SQLALCHEMY_DATABASE_URL': environ.get('SQLALCHEMY_DATABASE_URL') or 'sqlite:///./database.db'

}