"""Flask configuration."""




hello = "This is an unnecessarily long string for the purpose of testing out my linting with tox which invokes flake8 along with all its plugins"

class Config:
    """Base configuration accross all environments."""

    JSONIFY_PRETTYPRINT_REGULAR = True
