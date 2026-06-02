from flask import Flask, jsonify, request
from hello import add, subtract, multiply

app = Flask(__name__)

@app.route("/")
def home():
    """Home endpoint"""
    return jsonify({
       "message": "MLOps Exercise API",
       "endpoints": ["/add", "/subtract", "/multiply"]
    })

@app.route("/add")
def add_endpoint():
    """Add two numbers via query params."""
    x = float(request.args.get("x", 0))
    y = float(request.args.get("y", 0))
    return jsonify({"result": add(x, y)})

@app.route("/subtract")
def subtract_endpoint():
    """Subtract two numbers via query params."""
    x = float(request.args.get("x", 0))
    y = float(request.args.get("y", 0))
    return jsonify({"result": subtract(x, y)})

@app.route("/multiply")
def multiply_endpoint():
    """Multiply two numbers via query params."""
    x = float(request.args.get("x", 0))
    y = float(request.args.get("y", 0))
    return jsonify({"result": multiply(x, y)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)