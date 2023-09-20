from flask import jsonify, request
from werkzeug import exceptions
from application import app, db
from application.models import Quote
from .controllers import index


@app.route("/")
def hello_world():
    return jsonify({
        "message": "Welcome",
        "description": "Characters API",
        "endpoints": [
            "GET /",
            "GET /characters",
            "GET /characters/id",
            "POST /characters"
        ]
    }), 200


@app.route("/quotes")
def handle():
    return index()
