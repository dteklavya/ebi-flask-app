from os import getenv


class Config:
    """Set Flask configuration vars from environment."""


    # General Config
    FLASK_APP = getenv('FLASK_APP')
    FLASK_ENV = getenv('FLASK_ENV')

    # Database
    SQLALCHEMY_DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI")
