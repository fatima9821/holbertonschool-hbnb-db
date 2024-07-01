"""
Country related functionality
"""

from typing import Optional, List
from .base import SQLAlchemyBase
from . import db

class Country(SQLAlchemyBase):
    """Country representation"""

    __tablename__ = 'countries'

    name = db.Column(db.String(80), nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    cities = db.relationship('City', backref='country', lazy=True)

    def __init__(self, name: str, code: str, **kw) -> None:
        """Initialize a Country object"""
        super().__init__(**kw)
        self.name = name
        self.code = code

    def __repr__(self) -> str:
        """String representation of the Country object"""
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(country_data: dict) -> "Country":
        """Create a new country"""
        existing_country = Country.query.filter_by(code=country_data["code"]).first()
        if existing_country:
            raise ValueError("Country already exists")

        new_country = Country(**country_data)
        db.session.add(new_country)
        db.session.commit()
        return new_country

    @staticmethod
    def get(country_id: str) -> Optional["Country"]:
        """Retrieve a country by ID"""
        return Country.query.get(country_id)

    @staticmethod
    def get_all() -> List["Country"]:
        """Retrieve all countries"""
        return Country.query.all()

    @staticmethod
    def update(country_id: str, data: dict) -> Optional["Country"]:
        """Update an existing country"""
        country = Country.query.get(country_id)
        if not country:
            return None

        if "name" in data:
            country.name = data["name"]
        if "code" in data:
            country.code = data["code"]

        db.session.commit()
        return country

    @staticmethod
    def delete(country_id: str) -> bool:
        """Delete a country by ID"""
        country = Country.query.get(country_id)
        if not country:
            return False

        db.session.delete(country)
        db.session.commit()
        return True
