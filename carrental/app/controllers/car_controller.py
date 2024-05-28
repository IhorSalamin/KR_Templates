from flask import Blueprint, request, jsonify
from app.models.car import Car

car_controller = Blueprint('car_controller', __name__)

@car_controller.route('/cars', methods=['GET'])
def get_all_cars():
    cars = Car.get_all_cars()
    return jsonify([car.__dict__ for car in cars])

@car_controller.route('/car/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = Car.get_car_by_id(car_id)
    if car:
        return jsonify(car.__dict__)
    return jsonify({'error': 'Car not found'}), 404

@car_controller.route('/car', methods=['POST'])
def add_car():
    data = request.get_json()
    car_user_ref = data.get('car_user_ref')
    car_model = data.get('car_model')
    car_tier_ref = data.get('car_tier_ref')
    car_location = data.get('car_location')

    if not car_model:
        return jsonify({'error': 'Car model is required'}), 400

    Car.add_car(car_user_ref, car_model, car_tier_ref, car_location)
    return jsonify({'message': 'Car added successfully'}), 201

@car_controller.route('/car/report', methods=['GET'])
def get_car_report():
    report = Car.get_report()
    return jsonify(report)
