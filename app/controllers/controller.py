from app import app
from app.modules.calculator import add, subtract, divide, multiply



@app.route("/")
def greet():
    return "Welcome to the Calculator!"

@app.route("/add/<index1>/<index2>")
def addition(index1, index2):
    return str(add(int(index1), int(index2)))

@app.route("/subtract/<index1>/<index2>")
def minus(index1, index2):
    return str(subtract(int(index1), int(index2)))

@app.route("/multiply/<index1>/<index2>")
def times(index1, index2):
    return str(multiply(int(index1), int(index2)))

@app.route("/divide/<index1>/<index2>")
def div(index1, index2):
    return str(divide(int(index1), int(index2)))