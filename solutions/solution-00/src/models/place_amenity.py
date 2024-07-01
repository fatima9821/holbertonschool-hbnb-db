"""
Fonctionnalité liée à PlaceAmenity
"""

from typing import Optional
from .base import SQLAlchemyBase
from . import db

class PlaceAmenity(SQLAlchemyBase):
    """Représentation de PlaceAmenity"""                                                                                                         
    __tablename__ = 'place_amenities'
    __table_args__ = {'extend_existing': True}                                                                                                         
    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)                                                          
    amenity_id = db.Column(db.String(36), db.ForeignKey('amenities.id'), nullable=False)                                                      
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())                                           
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())                                                                           
    place = db.relationship("Place", back_populates="amenities")                                                        
    amenity = db.relationship("Amenity", back_populates="places")                                                                                                                            
                                                                                                     
    def __init__(self, place_id: str, amenity_id: str, **kw) -> None:        
        """Initialiser un objet PlaceAmenity"""                               
        super().__init__(**kw)                                               
        self.place_id = place_id                                             
        self.amenity_id = amenity_id                                                                                                          
                                                                                                     
    def __repr__(self) -> str:                                               
        """Représentation de chaîne de l'objet PlaceAmenity"""     
        return f"<PlaceAmenity ({self.place_id} - {self.amenity_id})>"

    def to_dict(self) -> dict:
        """Représentation dictionnaire de l'objet"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "amenity_id": self.amenity_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def get(place_id: str, amenity_id: str) -> Optional["PlaceAmenity"]:
        """Récupérer un PlaceAmenity par place_id et amenity_id"""             
        return PlaceAmenity.query.filter_by(place_id=place_id, amenity_id=amenity_id).first()                                                                                                                      
                                                                                                                     
    @staticmethod
    def create(data: dict) -> "PlaceAmenity":
        """Créer un nouveau PlaceAmenity"""
        new_place_amenity = PlaceAmenity(**data)
        db.session.add(new_place_amenity)
        db.session.commit()
        return new_place_amenity

    @staticmethod
    def delete(place_id: str, amenity_id: str) -> bool:
        """Supprimer un PlaceAmenity par place_id et amenity_id"""
        place_amenity = PlaceAmenity.get(place_id, amenity_id)
        if not place_amenity:
            return False

        db.session.delete(place_amenity)
        db.session.commit()
        return True

    @staticmethod
    def update(entity_id: str, data: dict):
        """Non implémenté, pas nécessaire"""
        raise NotImplementedError("Cette méthode est définie uniquement à cause de la classe Base")
