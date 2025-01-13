import pytest
from app import app


@pytest.fixture
def client():
    """Fixture to provide a test client."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test the homepage."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data



def test_bookings(client):
    """Test the bookings page."""
    response = client.get("/book")
    assert response.status_code == 200
