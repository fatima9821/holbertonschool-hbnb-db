"""
City related functionality
"""

from typing import Optional, List
from .base import SQLAlchemyBase
from . import db
from .country import Country

class City(SQLAlchemyBase):
    """City representation"""

    __tablename__ = 'cities'

    name = db.Column(db.String(128), nullable=False)
    country_code = db.Column(db.String(10), db.ForeignKey('countries.code'), nullable=False)
    country = db.relationship("Country", backref="cities")

    def __init__(self, name: str, country_code: str, **kw) -> None:
        """Initialize a City object"""
        super().__init__(**kw)
        self.name = name
        self.country_code = country_code

    def __repr__(self) -> str:
        """String representation of the City object"""
        return f"<City {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "country_code": self.country_code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "City":
        """Create a new city"""
        country = Country.query.filter_by(code=data["country_code"]).first()
        if not country:
            raise ValueError("Country not found")

        city = City(**data)
        db.session.add(city)
        db.session.commit()
        return city

    @staticmethod
    def get(city_id: str) -> Optional["City"]:
        """Retrieve a city by ID"""
        return City.query.get(city_id)

    @staticmethod
    def get_all() -> List["City"]:
        """Retrieve all cities"""
        return City.query.all()

    @staticmethod
    def update(city_id: str, data: dict) -> Optional["City"]:
        """Update an existing city"""
        city = City.query.get(city_id)
        if not city:
            return None

        for key, value in data.items():
            setattr(city, key, value)

        db.session.commit()
        return city

    @staticmethod
    def delete(city_id: str) -> bool:
        """Delete an existing city"""
        city = City.query.get(city_id)
        if not city:
            return False

        db.session.delete(city)
        db.session.commit()
        return True
