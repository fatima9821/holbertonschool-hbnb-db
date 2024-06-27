""" Another way to run the app"""

from flask import Flask
from models import db
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.place_amenity import PlaceAmenity
from models.country import Country


app = create_app()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

db.init_app(app)

with app.app_context():
    db.create_all()
