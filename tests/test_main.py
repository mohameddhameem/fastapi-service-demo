# Import necessary modules
import pytest
from fastapi.testclient import TestClient
from main import app

# Create a TestClient instance for making requests to the FastAPI instance
client = TestClient(app)

# Define a test function for the root endpoint
def test_root():
    # Make a GET request to the root endpoint
    response = client.get("/")
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response JSON matches the expected result
    assert response.json() == {"message": "Hello World"}

# Define a test function for the hello endpoint
def test_say_hello():
    # Make a GET request to the hello endpoint with a test name
    response = client.get("/hello/test")
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response JSON matches the expected result
    assert response.json() == {"message": "Hello test"}

# Define a test function for the form endpoint
def test_form():
    # Make a GET request to the form endpoint
    response = client.get("/form")
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

# Define a test function for the form submission endpoint
def test_form_post():
    # Make a POST request to the form submission endpoint with test data
    response = client.post("/submit_form", data={"name": "test", "address": "test address"})
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response JSON matches the expected result
    assert response.json() == {"name": "test", "address": "test address"}