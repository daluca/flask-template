"""Initialise Flask application."""
from flask import Flask

from project.config import config_map


def create_app(env="development", gunicorn_logger=None) -> Flask.app_context:
    """Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    cfg = config_map[env]
    app.config.from_object(cfg)

    if gunicorn_logger is not None:
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)

    with app.app_context():
        """Application context."""
        from project.blueprints import main_bp

        app.register_blueprint(main_bp)

        return app
