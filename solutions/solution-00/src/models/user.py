from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from src import db, bcrypt
from src import db

db = SQLALchemy()

class User(db.Model):
    """User representation"""

    __tablename__ = 'users'

    id = Column(String(36), primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_admin": self.is_admin,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(data):
        new_user = User(
            email=data.get('email'),
            password=data.get('password')
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def update(user_id, data):
        user = User.query.get(user_id)
        if not user:
            return None

        user.email = data.get('email', user.email)
        user.password = data.get('password', user.password)
        user.is_admin = data.get('is_admin', user.is_admin)
        db.session.commit()
        return user

    @staticmethod
    def delete(user_id):
        user = User.query.get(user_id)
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        return True
