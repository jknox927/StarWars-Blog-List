from flask import Flask, request, jsonify, url_for, Blueprint
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from api.models import db, User, People
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def index():
    response_body = {
        "message": "Welcome to StarWars REST API"
    }

    return jsonify(response_body), 200

@api.route('/login', methods=['POST'])
def login():
    req_username = request.json.get('username', None)
    get_user: User = User.query.filter_by(username = req_username).first()
    req_password = request.json.get('password', None)
    if get_user.password != req_password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity = username)
    return jsonify(access_token = access_token)

@api.route('/people', methods=['GET'])
def get_people():
    req_people: People = People.query.all()
    return jsonify(people = [people.serialize() for people in req_people])

@api.route('/people/<int:people_id>', methods=['GET'])
def get_person():
    person = People.query.filter_by(id=people_id).first()
    return jsonify(person.serialize())

@api.route('/films', methods=['GET'])
def get_films():
    return "films"

@api.route('/starships', methods=['GET'])
def get_starships():
    return "starships"

@api.route('/vehicles', methods=['GET'])
def get_vehicles():
    return "vehicles"

@api.route('/species', methods=['GET'])
def get_species():
    return "species"

@api.route('/planets', methods=['GET'])
def get_planets():
    return "planets"