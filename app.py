
from flask import Flask, jsonify

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route("/api/users")
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})

@app.route("/health")
def health_check():
    # Target Group health check endpoint
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
