""" Initialize the Flask app. """
import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from .models import db
from .data_manager import DataManager
from .config import DevelopmentConfig, ProductionConfig

cors = CORS()
jwt = JWTManager()

def create_app(config_class=DevelopmentConfig) -> Flask:
    """
    Create a Flask app with the given configuration class.
    The default configuration class is DevelopmentConfig.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Load environment variables from .env file
    load_dotenv()

    # Configure the app with the provided config class
    app.config.from_object(config_class)

    # Initialize CORS
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    # Initialize SQLAlchemy
    db.init_app(app)

    # Initialize JWT authentication
    jwt.init_app(app)

    # Create tables based on models
    with app.app_context():
        db.create_all()

    # Initialize DataManager with the app instance
    app.data_manager = DataManager(app)

    # Register routes and handlers
    register_routes(app)
    register_handlers(app)

    return app

def register_routes(app: Flask) -> None:
    """Import and register the routes for the Flask app"""

    # Import the routes here to avoid circular imports
    from src.routes.users import users_bp
    from src.routes.countries import countries_bp
    from src.routes.cities import cities_bp
    from src.routes.places import places_bp
    from src.routes.amenities import amenities_bp
    from src.routes.reviews import reviews_bp

    # Register the blueprints in the app
    app.register_blueprint(users_bp)
    app.register_blueprint(countries_bp)
    app.register_blueprint(cities_bp)
    app.register_blueprint(places_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(amenities_bp)

def register_handlers(app: Flask) -> None:
    """Register the error handlers for the Flask app."""
    app.errorhandler(404)(lambda e: (
        {"error": "Not found", "message": str(e)}, 404
    ))

    app.errorhandler(400)(lambda e: (
        {"error": "Bad request", "message": str(e)}, 400
    ))
