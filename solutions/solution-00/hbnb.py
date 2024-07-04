""" Another way to run the app """

from src import create_app, db
from src.models.user import User
from src.models.amenity import Amenity
from src.models.city import City
from src.models.state import State
from src.models.country import Country
from src.models.place import Place
from src.models.review import Review
from src.models.place_amenity import PlaceAmenity
from src.data_manager import DataManager
from dotenv import load_dotenv


load_dotenv()  

app = create_app()

with app.app_context():
    db.create_all()
    data_manager = DataManager(app)

if __name__ == "__main__":
    app.run()
