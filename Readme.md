# FastAPI Application

This is a simple FastAPI application that includes several endpoints for demonstration purposes. It uses Jinja2 for HTML templating and FastAPI's Form feature for handling form data.

## Endpoints

- `/`: Returns a simple JSON response.
- `/hello/{name}`: Returns a personalized hello message.
- `/form`: Displays a form.
- `/submit_form`: Handles form submission and returns the submitted data.

## Running Locally

1. Clone the repository: `git clone https://github.com/mohameddhameem/fastapi-service.git`
2. Navigate into the project directory: `cd fastapi-service`
3. Install the requirements: `pip install -r requirements.txt`
4. Run the application: `uvicorn main:app --reload`

The application will be available at `http://127.0.0.1:8000`.

## Running Tests

1. Run the tests: `pytest`

## Docker Build and Run

1. Build the Docker image: `docker build -t your-image-name .`
2. Run the Docker container: `docker run -p 80:80 your-image-name`

The application will be available at `http://localhost:80`.

## GitLab CI/CD Configuration

1. Create a `.gitlab-ci.yml` file in the root of your project.
2. Add the following configuration:

```yaml
image: python:3.9

stages:
    - build
    - test

build:
    stage: build
    script:
        - pip install -r requirements.txt

test:
    stage: test
    script:
        - pytest
```
---
