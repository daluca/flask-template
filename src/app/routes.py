"""Flask routes."""
from flask import Blueprint, render_template_string


main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/", methods=["GET"])
def index():
    """Homepage."""
    return render_template_string("Hello World!", status=200)
