""" Entry point for the application. """

from flask.cli import FlaskGroup
from flask_migrate import Migrate, MigrateCommand
from src import create_app, db

app = create_app()
cli = FlaskGroup(create_app=create_app)
migrate = Migrate(app, db)

# Ajoute la commande de gestion des migrations à FlaskGroup
cli.add_command('db', MigrateCommand)

if __name__ == "__main__":
    cli()
