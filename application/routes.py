from flask import jsonify, request
from werkzeug import exceptions
from application import app, db
from application.models import Quote
from .controllers import index, post, patch


@app.route("/")
def hello_world():
    return jsonify({
        "message": "Welcome",
        "description": "Kanye Quotes API",
        "endpoints": [
            "GET /"
        ]
    }), 200


@app.route("/quotes", methods=["GET", "POST", "PATCH"])
def handle():
    if request.method == "GET":
        return index()
    elif request.method == "POST":
        return post()
    elif request.method == "PATCH":
        return patch()
