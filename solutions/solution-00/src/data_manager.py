from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DataManager:
    """Class to manage data operations"""

    def __init__(self, app=None):
        self.app = app
        self.db = db
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize the Flask app with the database"""
        self.app = app
        self.db.init_app(app)

    def create(self, model, **kwargs):
        """Create a new instance of a model"""
        instance = model(**kwargs)
        self.db.session.add(instance)
        self.db.session.commit()
        return instance

    def get(self, model, id):
        """Retrieve an instance of a model by its ID"""
        return model.query.get(id)

    def update(self, instance):
        """Update an existing instance of a model"""
        self.db.session.commit()
        return instance

    def delete(self, instance):
        """Delete an instance of a model"""
        self.db.session.delete(instance)
        self.db.session.commit()

    def query_all(self, model):
        """Query all instances of a model"""
        return model.query.all()

    def get_or_create(self, model, defaults=None, **kwargs):
        """Retrieve an instance of a model or create it if it doesn't exist"""
        instance = model.query.filter_by(**kwargs).first()
        if instance:
            return instance, False
        else:
            params = {k: v for k, v in kwargs.items() if not isinstance(v, db.Model)}
            params.update(defaults or {})
            instance = model(**params)
            self.db.session.add(instance)
            self.db.session.commit()
            return instance, True
