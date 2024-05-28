from flask import Blueprint, request, jsonify
from app.models.message import Message

message_controller = Blueprint('message_controller', __name__)

@message_controller.route('/messages', methods=['GET'])
def get_all_messages():
    messages = Message.get_all_messages()
    return jsonify([message.__dict__ for message in messages])

@message_controller.route('/message', methods=['POST'])
def add_message():
    data = request.get_json()
    message_time = data.get('message_time')
    message_sender_ref = data.get('message_sender_ref')
    message_recipient_ref = data.get('message_recipient_ref')
    message_priority = data.get('message_priority')
    message_context = data.get('message_context')
    message_attachments = data.get('message_attachments')
    message_booking_ref = data.get('message_booking_ref')

    if not message_time or not message_sender_ref or not message_recipient_ref:
        return jsonify({'error': 'Missing required fields'}), 400

    Message.add_message(message_time, message_sender_ref, message_recipient_ref, message_priority, message_context, message_attachments, message_booking_ref)
    return jsonify({'message': 'Message added successfully'}), 201
