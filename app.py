from flask import Flask
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    with open("/app/logs/access.log", "a") as f:
        f.write(f"Accessed at {datetime.now()}\n")
    return {
        "message": "message": "CI/CD Pipeline Working Successfully",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.route("/health")
def health():
    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
