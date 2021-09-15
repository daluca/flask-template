"""Flask routes."""
from flask import Blueprint, render_template_string
from flask import current_app as app


main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/", methods=["GET"])
def index():
    """Homepage."""
    app.logger.debug("DEBUG message")
    app.logger.info("INFO message")
    app.logger.warning("WARN message")
    app.logger.error("ERROR message")
    app.logger.critical("CRITICAL message")
    return render_template_string("Hello World!", status=200)
