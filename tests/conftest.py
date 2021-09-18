"""pytest fixtures."""
import pytest

from project import create_app


@pytest.fixture(scope="module")
def test_client():
    """Testing flask application."""
    flask_app = create_app("testing")

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
