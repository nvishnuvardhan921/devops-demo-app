
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

@app.route("/about")
def about():
    return """
    <h1>DevOps Demo Application</h1>
    <p>This application is being used to learn DevOps.</p>
    <p>Tools: Git, GitHub, Jenkins, Docker, Kubernetes and AWS</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
