import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_duplicate():
    # Get an activity name
    activities = client.get("/activities").json()
    activity_name = next(iter(activities))
    email = "testuser@mergington.edu"
    # Signup
    signup = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup.status_code == 200
    # Duplicate signup
    duplicate = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert duplicate.status_code == 400
    assert "already signed up" in duplicate.json().get("detail", "")

# Add more tests for unregister and edge cases as needed
