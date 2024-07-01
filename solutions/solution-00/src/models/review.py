from typing import Optional, List
from .base_model import BaseModel
from . import db
from .place import Place  # Assurez-vous que l'importation est correcte ici

class Review(BaseModel):
    """Review representation"""

    __tablename__ = 'reviews'

    place_id = db.Column(db.String(36), db.ForeignKey('places.id'), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)

    place = db.relationship('Place', back_populates='reviews')
    user = db.relationship('User', back_populates='reviews')

    def __init__(self, place_id: str, user_id: str, text: str, **kwargs):
        """Initialize a Review object"""
        super().__init__(**kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text

    def __repr__(self) -> str:
        """String representation of the Review object"""
        return f"<Review {self.id} (Place: {self.place_id}, User: {self.user_id})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "text": self.text,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(review_data: dict) -> "Review":
        """Create a new review"""
        new_review = Review(**review_data)
        db.session.add(new_review)
        db.session.commit()
        return new_review

    @staticmethod
    def get(review_id: str) -> Optional["Review"]:
        """Retrieve a review by ID"""
        return Review.query.get(review_id)

    @staticmethod
    def get_all() -> List["Review"]:
        """Retrieve all reviews"""
        return Review.query.all()

    @staticmethod
    def update(review_id: str, data: dict) -> Optional["Review"]:
        """Update an existing review"""
        review = Review.query.get(review_id)

        if not review:
            return None

        if "place_id" in data:
            review.place_id = data["place_id"]
        if "user_id" in data:
            review.user_id = data["user_id"]
        if "text" in data:
            review.text = data["text"]

        db.session.commit()

        return review

    @staticmethod
    def delete(review_id: str) -> bool:
        """Delete a review by ID"""
        review = Review.query.get(review_id)
        if not review:
            return False

        db.session.delete(review)
        db.session.commit()
        return True
