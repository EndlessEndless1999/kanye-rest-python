from flask import jsonify, request
from werkzeug import exceptions
from .models import Quote
from . import db


def index():
    try:
        quotes = Quote.query.all()
        data = [q.json for q in quotes]
        return jsonify({"quotes": data})
    except:
        raise exceptions.InternalServerError

def patch():
    pass


def post():
    try:
        print("🌕🌕🌕🌕", request.json)
        id, quote = request.json.values()
        new_quote = Quote(quote=quote)

        db.session.add(new_quote)
        db.session.commit()

        return jsonify({"data": new_quote.json}), 201
    except:
        print("❌❌❌", request)
        raise exceptions.BadRequest(f"We cannot process your request")


