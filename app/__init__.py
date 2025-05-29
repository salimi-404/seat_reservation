from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    app.config.from_mapping(
        total_seats=100,
        num_threads=100,
        max_request=4,
        cancellation_chance=0.3
    )

    return app
