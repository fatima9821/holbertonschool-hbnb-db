from typing import Optional, List
from .base_model import BaseModel
from . import db

class User(BaseModel):
    """User representation"""

    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())

    def __init__(self, email: str, first_name: str, last_name: str, password: str, is_admin: bool = False, **kw):
        """Initialize a User object"""
        super().__init__(**kw)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.is_admin = is_admin

    def __repr__(self) -> str:
        """String representation of the User object"""
        return f"<User {self.id} ({self.email})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(user_data: dict) -> "User":
        """Create a new user"""
        existing_user = User.query.filter_by(email=user_data["email"]).first()
        if existing_user:
            raise ValueError("User already exists")

        new_user = User(**user_data)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get(user_id: str) -> Optional["User"]:
        """Retrieve a user by ID"""
        return User.query.get(user_id)

    @staticmethod
    def get_all() -> List["User"]:
        """Retrieve all users"""
        return User.query.all()

    @staticmethod
    def update(user_id: str, data: dict) -> Optional["User"]:
        """Update an existing user"""
        user = User.query.get(user_id)

        if not user:
            return None

        if "email" in data:
            user.email = data["email"]
        if "first_name" in data:
            user.first_name = data["first_name"]
        if "last_name" in data:
            user.last_name = data["last_name"]
        if "password" in data:
            user.password = data["password"]
        if "is_admin" in data:
            user.is_admin = data["is_admin"]

        db.session.commit()

        return user

    @staticmethod
    def delete(user_id: str) -> bool:
        """Delete a user by ID"""
        user = User.query.get(user_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        return True
