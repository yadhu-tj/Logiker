from fastapi import FastAPI # 1. Import FastAPI class

# app= variable name for the FastAPI instance
# Created a FastAPI instance
app = FastAPI()


@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Yo {name}, welcome to the backend!"}

# @ is a decorator
# Decorator to define a route for HTTP GET requests at the root URL ("/")
@app.get("/")
def read_root(): # Function to handle requests to the root URL
    return {"Hello": "the project is alive"} # Return a JSON response for this route

