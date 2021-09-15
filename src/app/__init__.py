"""Initialise Flask application."""
from flask import Flask


def create_app():
    """Flask application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        from app.routes import main_bp

        app.register_blueprint(main_bp)

        return app
