from flask import Blueprint, request, jsonify
from app.models.booking import Booking

booking_controller = Blueprint('booking_controller', __name__)

@booking_controller.route('/bookings', methods=['GET'])
def get_all_bookings():
    bookings = Booking.get_all_bookings()
    return jsonify([booking.__dict__ for booking in bookings])

@booking_controller.route('/booking/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = Booking.get_booking_by_id(booking_id)
    if booking:
        return jsonify(booking.__dict__)
    return jsonify({'error': 'Booking not found'}), 404

@booking_controller.route('/booking', methods=['POST'])
def create_booking():
    data = request.get_json()
    booking_driver_ref = data.get('booking_driver_ref')
    booking_customer_ref = data.get('booking_customer_ref')
    booking_time = data.get('booking_time')
    booking_duration = data.get('booking_duration')
    booking_status = data.get('booking_status')
    booking_start_point = data.get('booking_start_point')
    booking_end_point = data.get('booking_end_point')

    if not booking_driver_ref or not booking_customer_ref or not booking_time or not booking_duration or not booking_status or not booking_start_point:
        return jsonify({'error': 'Missing required fields'}), 400

    Booking.create_booking(booking_driver_ref, booking_customer_ref, booking_time, booking_duration, booking_status, booking_start_point, booking_end_point)
    return jsonify({'message': 'Booking created successfully'}), 201
