"""Initialise Flask application."""
import logging

from flask import Flask


def create_app(gunicorn_logger=None) -> Flask.app_context:
    """Flask application."""
    app = Flask(__name__)
    app.config.from_object("config.Config")

    if gunicorn_logger is not None:
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel = gunicorn_logger.level
    else:
        app.logger.setLevel = logging.DEBUG

    with app.app_context():
        """Application context."""
        from app.routes import main_bp

        app.register_blueprint(main_bp)

        return app
