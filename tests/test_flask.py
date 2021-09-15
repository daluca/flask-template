"""Flask application testing."""


def test_flask():
    """Get better testing doc string."""
    x = str
    assert x == str


def test_python_version():
    """Bad doc string."""
    x = 6
    y = f"{x = }"

    assert y == "x = 6"
    assert type(y) == str
