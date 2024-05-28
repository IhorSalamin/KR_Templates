from flask import Blueprint, request, jsonify
from app.models.server import Server

server_controller = Blueprint('server_controller', __name__)

@server_controller.route('/servers', methods=['GET'])
def get_all_servers():
    servers = Server.get_all_servers()
    return jsonify([server.__dict__ for server in servers])

@server_controller.route('/server/<int:server_id>', methods=['GET'])
def get_server(server_id):
    server = Server.get_server_by_id(server_id)
    if server:
        return jsonify(server.__dict__)
    return jsonify({'error': 'Server not found'}), 404

@server_controller.route('/server', methods=['POST'])
def add_server():
    data = request.get_json()
    server_status = data.get('server_status')
    server_location = data.get('server_location')

    if not server_status or not server_location:
        return jsonify({'error': 'Missing required fields'}), 400

    Server.add_server(server_status, server_location)
    return jsonify({'message': 'Server added successfully'}), 201
