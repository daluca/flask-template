"""Flask routes functional route tests."""


def test_get_index(test_client):
    """
    Test the index endpoint.

    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Hello World!" in response.data


def test_post_index(test_client):
    """
    Test the index endpoint.

    GIVEN a Flask application configured for testing
    WHEN the '/' page is required (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post("/")
    assert response.status_code == 405
    assert b"Hello World!" not in response.data
