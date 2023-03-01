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
            "profile_pic": self.profile_pic,
            "username": self.username,
            "is_active": self.is_active
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


class Films(db.Model):
    __tablename__ = 'films'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    episode_id = db.Column(db.Integer)
    opening_crawl = db.Column(db.String(256))
    director = db.Column(db.String(128))
    producer = db.Column(db.String(128))
    # release_date = db.Column(db.Datetime, default=datetime.date())
    url = db.Column(db.String(256))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_edited = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Films {self.title}>'

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "episode_id": self.episode_id,
            "opening_crawl": self.opening_crawl,
            "director": self.director,
            "producer": self.producer,
            # "release_date": self.release_date,
            "url": self.url,
            "date_created": self.date_created,
            "date_edited": self.date_edited
        }


class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    model = db.Column(db.String(128))
    starship_class = db.Column(db.String(128))
    manufacturer = db.Column(db.String(128))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    hyperdrive_rating = db.Column(db.String(64))
    MGLT = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.Integer)
    url = db.Column(db.String(64))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_edited = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Starships {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.nae,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "url": self.url,
            "date_created": self.date_created,
            "date_edited": self.date_edited
        }