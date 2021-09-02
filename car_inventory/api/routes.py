import re
from flask import Blueprint, request, jsonify
from car_inventory.helpers import token_required
from car_inventory.models import db, User, Car, car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def get_data(current_user_token):
    return {'some' : 'value'}

# CREATE CAR ENDPOINT
@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    make = request.json['make']
    _model = request.json['model']
    year = request.json['year']
    price = request.json['price']
    seats = request.json['seats']
    transmission = request.json['transmission']
    engine = request.json['engine']
    dimensions = request.json['dimensions']
    weight = request.json['weight']
    MSRP = request.json['MSRP']
    user_token = current_user_token.token

    car = Car(make, _model, year, price, seats, transmission, engine, dimensions, weight, MSRP, user_token)
    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

# RETRIEVE ALL CARS ENDPOINT

@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(cars)
    return jsonify(response)

# RETRIEVE ONE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        car = Car.query.get(id)
        response = car_schema.dump(car)
        return jsonify(response)
    else: 
        return jsonify({'message': 'Valid Token Required'}),401

# UPDATE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['POST','PUT'])
@token_required
def update_car(current_user_token, id):
    car = Car.query.get(id) # Get Drone Instance
    car.make = request.json['make']
    car._model = request.json['_model']
    car.year = request.json['year']
    car.price = request.json['price']
    car.seats = request.json['seats']
    car.transmission = request.json['transmission']
    car.engine = request.json['engine']
    car.dimensions = request.json['dimensions']
    car.weight = request.json['weight']
    car.MSRP = request.json['MSRP']
    car.user_token = current_user_token.token

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

# DELETE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)
