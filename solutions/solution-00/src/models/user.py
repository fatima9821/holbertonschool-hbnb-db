from datetime import datetime
from sqlalchemy import Column, String, Boolean
from src import db, bcrypt  # Assurez-vous que 'db' et 'bcrypt' sont correctement importés

class User(db.Model):
    """User representation"""

    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, email, password, is_admin=False):
        self.email = email
        self.set_password(password)
        self.is_admin = is_admin

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

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
        password = data.get('password')
        if password:
            user.set_password(password)
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
