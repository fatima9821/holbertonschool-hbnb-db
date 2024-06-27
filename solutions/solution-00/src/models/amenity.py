"""
Amenity related functionality
"""

from . import db
from src.models.base import Base
from datetime import datetime


class Amenity(Base):
    """Amenity representation"""

    __tablename__ = 'amenities'

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, name: str, **kw) -> None:
        """Dummy init"""
        super().__init__(**kw)

        self.name = name

    def __repr__(self) -> str:
        """Dummy repr"""
        return f"<Amenity {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data: dict) -> "Amenity":
        """Create a new amenity"""
        existing_amenity = Amenity.query.filter_by(name=data["name"]).first()
        if existing_amenity:
            raise ValueError("Amenity already exists")

        amenity = Amenity(**data)
        db.session.add(amenity)
        db.session.commit()
        return amenity

    @staticmethod
    def update(amenity_id: str, data: dict) -> "Amenity | None":
        """Update an existing amenity"""
        from src.persistence import repo

        amenity: Amenity | None = Amenity.get(amenity_id)

        if not amenity:
            return None

        if "name" in data:
            amenity.name = data["name"]

        repo.update(amenity)

        return amenity

    class PlaceAmenity(db.Model):
    """PlaceAmenity representation"""

    __tablename__ = 'place_amenities'

    id = db.Column(db.String(36), primary_key=True)
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    amenity_id = db.Column(db.String(36), db.ForeignKey('amenities.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    place = db.relationship("Place", back_populates="amenities")
    amenity = db.relationship("Amenity", back_populates="places")

    def __init__(self, place_id: str, amenity_id: str, **kw) -> None:
        """Init method"""
        super().__init__(**kw)
        self.place_id = place_id
        self.amenity_id = amenity_id

    def __repr__(self) -> str:
        """Representation method"""
        return f"<PlaceAmenity ({self.place_id} - {self.amenity_id})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "amenity_id": self.amenity_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def get(place_id: str, amenity_id: str) -> "PlaceAmenity | None":
        """Get a PlaceAmenity object by place_id and amenity_id"""
        return PlaceAmenity.query.filter_by(place_id=place_id, amenity_id=amenity_id).first()

    @staticmethod
    def create(data: dict) -> "PlaceAmenity":
        """Create a new PlaceAmenity object"""
        new_place_amenity = PlaceAmenity(**data)
        db.session.add(new_place_amenity)
        db.session.commit()
        return new_place_amenity

    @staticmethod
    def delete(place_id: str, amenity_id: str) -> bool:
        """Delete a PlaceAmenity object by place_id and amenity_id"""
        place_amenity = PlaceAmenity.get(place_id, amenity_id)
        if not place_amenity:
            return False

        db.session.delete(place_amenity)
        db.session.commit()
        return True

    @staticmethod
    def update(entity_id: str, data: dict):
        """Not implemented, isn't needed"""
        raise NotImplementedError("This method is defined only because of the Base class")
