from os import getenv, path
from dotenv import load_dotenv


class Config:
    """Set Flask configuration vars from environment."""


    APP_ROOT = path.join(path.dirname(__file__))   # refers to application_top
    dotenv_path = path.join(APP_ROOT, '.env')
    load_dotenv(dotenv_path=dotenv_path)

    # General Config
    FLASK_APP = getenv('FLASK_APP')
    FLASK_ENV = getenv('FLASK_ENV')

    # Database
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
