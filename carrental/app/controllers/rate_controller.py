from flask import Blueprint, request, jsonify
from app.models.rate import Rate

rate_controller = Blueprint('rate_controller', __name__)

@rate_controller.route('/rates', methods=['GET'])
def get_all_rates():
    rates = Rate.get_all_rates()
    return jsonify([rate.__dict__ for rate in rates])

@rate_controller.route('/rate/<int:rate_id>', methods=['GET'])
def get_rate(rate_id):
    rate = Rate.get_rate_by_id(rate_id)
    if rate:
        return jsonify(rate.__dict__)
    return jsonify({'error': 'Rate not found'}), 404

@rate_controller.route('/rate', methods=['POST'])
def add_rate():
    data = request.get_json()
    rate_sender_ref = data.get('rate_sender_ref')
    rate_recipient_ref = data.get('rate_recipient_ref')
    rate_stars = data.get('rate_stars')
    rate_description = data.get('rate_description')

    if not rate_sender_ref or not rate_recipient_ref or not rate_stars:
        return jsonify({'error': 'Missing required fields'}), 400

    Rate.add_rate(rate_sender_ref, rate_recipient_ref, rate_stars, rate_description)
    return jsonify({'message': 'Rate added successfully'}), 201
