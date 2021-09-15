"""WSGI entrypoint."""
import logging

from app import create_app


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    application = create_app(gunicorn_logger=gunicorn_logger)
else:
    application = create_app()
