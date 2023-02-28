from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    profile_pic = db.Column(db.String(128), nullable=True)
    username = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    birth_year = db.Column(db.String(256))
    eye_color = db.Column(db.String(256))
    gender = db.Column(db.String(256))
    hair_color = db.Column(db.String(256))
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    skin_color = db.Column(db.String(256))
    homeworld = db.Column(db.String(256))
    url = db.Column(db.String(256))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_edited = db.Column(db.DateTime, default=datetime.utcnow)

    # films_rel = db.relationship('Films', backref='films', uselist=True)
    # films_id = db.Column(db.Integer, db.ForeignKey('films.id'))

    # species_rel = db.relationship('Species', backref='species', uselist=True)
    # species_id = db.Column(db.Integer, db.ForeignKey('species.id'))

    # starships_rel = db.relationship('Starships', backref='starships', uselist=True)
    # starships_id = db.Column(db.Integer, db.ForeignKey('starships.id'))

    # vehicles_rel = db.relationship('Vehicles', backref='vehicles', uselist=True)
    # vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    def __repr__(self):
        return f'<People {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "homeworld": self.homeworld,
            "url": self.url,
            "date_created": self.date_created,
            "date_edited": self.date_edited
        }