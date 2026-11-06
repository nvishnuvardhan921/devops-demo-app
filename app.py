
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>DevOps Demo Application</h1>
    <h2>Application Status: Running</h2>
    <p>Version: 1.0</p>
    <p>Welcome to my DevOps learning project!</p>
    """


@app.route("/health")
def health():
    return jsonify(
        status="UP",
        application="devops-demo-app",
        version="1.0"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
