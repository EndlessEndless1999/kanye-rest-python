from flask import jsonify
from werkzeug import exceptions
from .models import Quote


def index():
    try:
        quotes = Quote.query.all()
        data = [q.json for q in quotes]
        return jsonify({"quotes": data})
    except:
        raise exceptions.InternalServerError

