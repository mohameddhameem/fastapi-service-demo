# Import necessary modules from FastAPI
from fastapi import FastAPI, Request, Form
# Import Jinja2Templates for rendering HTML templates
from fastapi.templating import Jinja2Templates

# Create a FastAPI instance
app = FastAPI()

# Create a Jinja2Templates instance with the directory of templates
templates = Jinja2Templates(directory="templates")

# Define a route for the root ("/") URL
@app.get("/")
async def root():
    # Return a simple JSON response
    return {"message": "Hello World"}

# Define a route for saying hello to a user
@app.get("/hello/{name}")
async def say_hello(name: str):
    # Return a personalized hello message
    return {"message": f"Hello {name}"}

# Define a route for displaying a form
@app.get("/form")
async def form(request: Request):
    # Render the form.html template
    return templates.TemplateResponse("form.html", {"request": request})

# Define a route for submitting the form
@app.post("/submit_form")
async def form_post(request: Request, name: str = Form(...), address: str = Form(...)):
    # Return the submitted form data
    return {"name": name, "address": address}
