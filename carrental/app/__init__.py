from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    with app.app_context():
        from app.controllers.user_controller import user_controller
        from app.controllers.car_controller import car_controller
        from app.controllers.message_controller import message_controller
        
        app.register_blueprint(user_controller, url_prefix='/api')
        app.register_blueprint(car_controller, url_prefix='/api')
        app.register_blueprint(message_controller, url_prefix='/api')

    return app
