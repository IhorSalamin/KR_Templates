from flask import Flask, request
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Налаштовуємо CORS для всього додатку з дозволом всіх методів та заголовків
    CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": ["Content-Type", "Authorization"]}})

    # Додаємо обробку для запитів OPTIONS
    @app.before_request
    def handle_options_requests():
        if request.method == 'OPTIONS':
            return '', 200

    with app.app_context():
        from app.controllers.user_controller import user_controller
        from app.controllers.car_controller import car_controller
        from app.controllers.message_controller import message_controller
        from app.controllers.booking_controller import booking_controller
        from app.controllers.rate_controller import rate_controller
        from app.controllers.tier_controller import tier_controller
        from app.controllers.server_controller import server_controller
        
        app.register_blueprint(user_controller, url_prefix='/api')
        app.register_blueprint(car_controller, url_prefix='/api')
        app.register_blueprint(message_controller, url_prefix='/api')
        app.register_blueprint(booking_controller, url_prefix='/api')
        app.register_blueprint(rate_controller, url_prefix='/api')
        app.register_blueprint(tier_controller, url_prefix='/api')
        app.register_blueprint(server_controller, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
