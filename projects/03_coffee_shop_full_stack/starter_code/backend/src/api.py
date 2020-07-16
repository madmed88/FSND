import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

db_drop_and_create_all()

# ROUTES


@app.route('/drinks')
def get_drinks():
    return jsonify({
        'success': True,
        'drinks': [drink.short() for drink in Drink.query.all()]
    })


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drink():
    return jsonify({
        'success': True,
        'drinks': [drink.long() for drink in Drink.query.all()]
    })


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_drink():
    data = request.get_json()
    if('title' not in data or 'recipe' not in data):
        abort(422)

    title = data.get('title', None)
    recipe = data.get('recipe', None)
    drink = Drink(title=title, recipe=json.dumps(recipe))
    drink.insert()
    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    })


@app.route('/drinks/<drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def edit_drink(drink_id):
    data = request.get_json()
    if('title' not in data and 'recipe' not in data):
        abort(422)

    drink = Drink.query.get(drink_id)
    drink.title = data.get('title', drink.title)
    drink.recipe = data.get('recipe', drink.recipe)
    drink.update()
    return jsonify({
        'success': True,
        'drinks': [drink.long()]
    })


@app.route('/drinks/<drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(drink_id):
    drink = Drink.query.get(drink_id)
    if(drink is None):
        abort(404)
    drink.delete()
    return jsonify({
        'success': True,
        'delete': drink_id
    })


# Error Handling
'''
Example error handling for unprocessable entity
'''


@ app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@ app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@ app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


@ app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error
    }), error.status_code
