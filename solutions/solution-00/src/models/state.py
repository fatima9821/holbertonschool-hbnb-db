"""
State related functionality
"""

from typing import Optional, List
from .base import SQLAlchemyBase
from . import db

class State(SQLAlchemyBase):
    """State representation"""

    __tablename__ = 'states'

    name = db.Column(db.String(128), nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    cities = db.relationship('City', backref='state', lazy=True)

    def __init__(self, name: str, code: str, **kw) -> None:
        """Initialize a State object"""
        super().__init__(**kw)
        self.name = name
        self.code = code

    def __repr__(self) -> str:
        """String representation of the State object"""
        return f"<State {self.code} ({self.name})>"

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
    def create(state_data: dict) -> "State":
        """Create a new state"""
        existing_state = State.query.filter_by(code=state_data["code"]).first()
        if existing_state:
            raise ValueError("State already exists")

        new_state = State(**state_data)
        db.session.add(new_state)
        db.session.commit()
        return new_state

    @staticmethod
    def get(state_id: str) -> Optional["State"]:
        """Retrieve a state by ID"""
        return State.query.get(state_id)

    @staticmethod
    def get_all() -> List["State"]:
        """Retrieve all states"""
        return State.query.all()

    @staticmethod
    def update(state_id: str, data: dict) -> Optional["State"]:
        """Update an existing state"""
        state = State.query.get(state_id)
        if not state:
            return None

        for key, value in data.items():
            setattr(state, key, value)

        db.session.commit()
        return state

    @staticmethod
    def delete(state_id: str) -> bool:
        """Delete an existing state"""
        state = State.query.get(state_id)
        if not state:
            return False

        db.session.delete(state)
        db.session.commit()
        return True
