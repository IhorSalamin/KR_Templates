from flask import Blueprint, request, jsonify
from app.models.user import User

user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_user_by_id(user_id)
    if user:
        return jsonify(user.__dict__)
    return jsonify({'error': 'User not found'}), 404

@user_controller.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_name = data.get('user_name')
    user_email = data.get('user_email')
    user_phone = data.get('user_phone')
    user_password = data.get('user_password')
    user_gender = data.get('user_gender', '')
    user_role = data.get('user_role', '')
    user_details = data.get('user_details', '')

    if not user_name or not user_email or not user_phone or not user_password:
        return jsonify({'error': 'Missing required fields'}), 400

    User.create_user(user_name, user_email, user_phone, user_password, user_gender, user_role, user_details)
    return jsonify({'message': 'User created successfully'}), 201

@user_controller.route('/users', methods=['GET'])
def get_all_users():
    users = User.get_all_users()
    return jsonify([user.__dict__ for user in users])
