""" Initialize the Flask app. """
import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
cors = CORS()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app(config_class="src.config.DevelopmentConfig"):
    """
    Create a Flask app with the given configuration class.
    The default configuration class is DevelopmentConfig.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    env = os.getenv('ENV', 'development')
    
    if env == 'development':
        app.config.from_object('src.config.DevelopmentConfig')
    else:
        app.config.from_object('src.config.ProductionConfig')

    db.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})
    jwt.init_app(app)
    bcrypt.init_app(app)

    register_routes(app)
    register_handlers(app)

    return app

def register_routes(app):
    """Import and register the routes for the Flask app"""

    # Importez vos blueprints ici
    from src.routes.users import users_bp
    from src.routes.countries import countries_bp
    from src.routes.cities import cities_bp

    # Enregistrez les blueprints dans l'application
    app.register_blueprint(users_bp)
    app.register_blueprint(countries_bp)
    app.register_blueprint(cities_bp)

def register_handlers(app):
    """Register the error handlers for the Flask app."""
    app.errorhandler(404)(
        lambda e: ({"error": "Not found", "message": str(e)}, 404)
    )
    app.errorhandler(400)(
        lambda e: ({"error": "Bad request", "message": str(e)}, 400)
    )
