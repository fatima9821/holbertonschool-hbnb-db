""" Another way to run the app"""

from src import create_app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = create_app()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run()
