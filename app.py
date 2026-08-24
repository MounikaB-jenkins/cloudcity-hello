from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Master Test!"

@app.route("/about")
def about():
    return "This is CloudCity v3!"

@app.route("/hello", methods=["POST"])
def hello_post():
    data = request.get_json()
    name = data.get("name", "CloudCity")
    return f"Hello, {name}!"

@app.route("/slow")
def slow():
    time.sleep(10)
    return "Slow response finished!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)