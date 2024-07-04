"""
This module exports configuration classes for the Flask application.

- DevelopmentConfig
- TestingConfig
- ProductionConfig
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """
    Initial configuration settings.
    This class should not be instantiated directly.
    """

    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configuration settings.
    This configuration is used when running the application locally.
    It's useful for development and debugging purposes.
    """

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///development.db")
    DEBUG = True


class TestingConfig(Config):
    """
    Testing configuration settings.
    This configuration is used when running tests.
    """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class ProductionConfig(Config):
    """
    Production configuration settings.
    This configuration is used for the production build of the application.
    The debug or testing options are disabled in this configuration.
    """

    TESTING = False
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost/hbnb_prod"
    )
