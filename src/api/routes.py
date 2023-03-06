from flask import Flask, request, jsonify, url_for, Blueprint
# from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from api.models import db, User, People, Films, Starships
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)

# @api.route('/login', methods=['POST'])
# def login():
#     req_username = request.json.get('username', None)
#     get_user: User = User.query.filter_by(username = req_username).first()
#     req_password = request.json.get('password', None)
#     if get_user.password != req_password:
#         return jsonify({"msg": "Bad username or password"}), 401

#     access_token = create_access_token(identity = username)
#     return jsonify(access_token = access_token)

@api.route('/people', methods=['GET'])
def get_people():
    req_people: People = People.query.all()
    return jsonify(people = [people.serialize() for people in req_people])

@api.route('/people/<int:people_id>', methods=['GET'])
def get_people_by_id(people_id):
    people = People.query.get_or_404(people_id, description='Person not found...')
    people_id = people.serialize()
    db.session.commit()
    return jsonify(people_id), 200

@api.route('/people', methods=['POST'])
def add_people():
    req_body_user = request.get_json()
    return 'No Idea...'

@api.route('/films', methods=['GET'])
def get_films():
    req_films: Films = Films.query.all()
    return jsonify(films = [films.serialize() for films in req_films])

@api.route('/starships', methods=['GET'])
def get_starships():
    req_starships: Starships = Starships.query.all()
    return jsonify(starships = [starships.serialize() for starships in req_starships])



# Placeholder routes to finish later

@api.route('/vehicles', methods=['GET'])
def get_vehicles():
    return "vehicles"

@api.route('/species', methods=['GET'])
def get_species():
    return "species"

@api.route('/planets', methods=['GET'])
def get_planets():
    return "planets"