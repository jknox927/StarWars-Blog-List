"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, People
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


# @api.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#     response_body = {
#         "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
#     }

#     return jsonify(response_body), 200

@api.route('/', methods=['GET'])
def home():
    response_body = {
        "message": "Welcome to StarWars REST API"
    }

    return jsonify(response_body), 200

@api.route('/people', methods=['GET'])
def get_people():
    return People.name

@api.route('/people/<int:people_id>', methods=['GET'])
def get_peopleDetails():
    return "people_id"

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