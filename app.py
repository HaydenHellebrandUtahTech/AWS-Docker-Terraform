from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "AWS Docker Terraform API is running!",
        "status": "online",
        "platform": "AWS ECS Fargate"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200
