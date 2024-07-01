"""
Place related functionality
"""
from datetime import datetime
import uuid
from typing import Optional, List
from . import db
from .base import SQLAlchemyBase
from .city import City
from .user import User
from .place_amenity import PlaceAmenity  # Assurez-vous que PlaceAmenity est importé correctement

class Place(SQLAlchemyBase):
    """Place representation"""

    __tablename__ = 'places'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=True)
    address = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    host_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    city_id = db.Column(db.String(36), db.ForeignKey('cities.id'), nullable=False)
    price_per_night = db.Column(db.Integer, nullable=False)
    number_of_rooms = db.Column(db.Integer, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)

    host = db.relationship("User", back_populates="places")
    city = db.relationship("City", back_populates="places")
    amenities = db.relationship("PlaceAmenity", back_populates="place", cascade="all, delete-orphan")
    reviews = db.relationship('Review', back_populates='place')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.address = kwargs.get("address", "")
        self.latitude = float(kwargs.get("latitude", 0.0))
        self.longitude = float(kwargs.get("longitude", 0.0))
        self.host_id = kwargs["host_id"]
        self.city_id = kwargs["city_id"]
        self.price_per_night = int(kwargs.get("price_per_night", 0))
        self.number_of_rooms = int(kwargs.get("number_of_rooms", 0))
        self.number_of_bathrooms = int(kwargs.get("number_of_bathrooms", 0))
        self.max_guests = int(kwargs.get("max_guests", 0))

    def __repr__(self) -> str:
        """String representation of the Place object"""
        return f"<Place {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "city_id": self.city_id,
            "host_id": self.host_id,
            "price_per_night": self.price_per_night,
            "number_of_rooms": self.number_of_rooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "max_guests": self.max_guests,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "Place":
        """Create a new place"""
        host = User.query.get(data["host_id"])
        if not host:
            raise ValueError(f"User with ID {data['host_id']} not found")

        city = City.query.get(data["city_id"])
        if not city:
            raise ValueError(f"City with ID {data['city_id']} not found")

        place = Place(**data)
        db.session.add(place)
        db.session.commit()
        return place

    @staticmethod
    def update(place_id: str, data: dict) -> Optional["Place"]:
        """Update an existing place"""
        place = Place.query.get(place_id)
        if not place:
            return None

        for key, value in data.items():
            setattr(place, key, value)

        db.session.commit()
        return place

    @staticmethod
    def delete(place_id: str) -> bool:
        """Delete an existing place"""
        place = Place.query.get(place_id)
        if not place:
            return False

        db.session.delete(place)
        db.session.commit()
        return True
