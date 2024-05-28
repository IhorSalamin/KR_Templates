from flask import Blueprint, request, jsonify
from app.models.tier import Tier

tier_controller = Blueprint('tier_controller', __name__)

@tier_controller.route('/tiers', methods=['GET'])
def get_all_tiers():
    tiers = Tier.get_all_tiers()
    return jsonify([tier.__dict__ for tier in tiers])

@tier_controller.route('/tier/<int:tier_id>', methods=['GET'])
def get_tier(tier_id):
    tier = Tier.get_tier_by_id(tier_id)
    if tier:
        return jsonify(tier.__dict__)
    return jsonify({'error': 'Tier not found'}), 404

@tier_controller.route('/tier', methods=['POST'])
def add_tier():
    data = request.get_json()
    tier_name = data.get('tier_name')
    tier_price = data.get('tier_price')
    tier_order = data.get('tier_order')

    if not tier_name or not tier_price or not tier_order:
        return jsonify({'error': 'Missing required fields'}), 400

    Tier.add_tier(tier_name, tier_price, tier_order)
    return jsonify({'message': 'Tier added successfully'}), 201
