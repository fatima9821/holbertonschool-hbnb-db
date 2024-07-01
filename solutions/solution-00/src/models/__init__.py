from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .amenity import Amenity
from .place import Place
from .city import City
from .state import State
from .place_amenity import PlaceAmenity
from .country import Country
from .review import Review
from .place_amenity import PlaceAmenity
