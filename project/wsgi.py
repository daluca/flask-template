"""WSGI entrypoint to Flask application."""
import logging
from os import getenv

from project import create_app


env = getenv("FLASK_ENV", "development")


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    application = create_app(env=env, gunicorn_logger=gunicorn_logger)
else:
    application = create_app(env=env)
    application.run()
