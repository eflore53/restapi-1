import random
import string
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from random import randint
app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# @app.route('/users')
# def get_users():
#     # accessing the value of parameter 'name'
#     search_username = request.args.get('name')
#     if search_username:
#         subdict = {'users_list': []}
#         for user in users['users_list']:
#             if user['name'] == search_username:
#                 subdict['users_list'].append(user)
#         return subdict
#     return users


@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if id:
        for user in users['users_list']:
            if user['id'] == id:
                if request.method == 'GET':
                    return user
                elif request.method == 'DELETE':
                    users['users_list'].remove(user)
                    resp = jsonify(), 204
                    return resp
        resp = jsonify({"Msg": "Resource not found."}), 404
        return resp
    return users


# @app.route('/users/<id>')
# def get_user(id):
#     if id:
#         for user in users['users_list']:
#             if user['id'] == id:
#                 return user
#         return ({})
#     return users


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        if search_username and search_job:
            return find_users_by_name_job(search_username, search_job)
        elif search_username:
            return find_users_by_name(search_username)
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = random_id()
        users['users_list'].append(userToAdd)
        resp = jsonify(userToAdd), 201
        # returning 201 and attaching json object
        # resp.status_code = 200 #optionally, you can always set a response code.
        # 200 is the default code for a normal response
        return resp


def random_id():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    personId = random.choice(letters)
    personId += random.choice(letters)
    personId += random.choice(letters)
    personId += str(randint(0, 9))
    personId += str(randint(0, 9))
    personId += str(randint(0, 9))
    return personId


def find_users_by_name_job(name, job):
    subdict = {'users_list': []}
    for user in users['users_list']:
        if user['name'] == name and user['job'] == job:
            subdict['users_list'].append(user)
    return subdict


def find_users_by_name(name):
    subdict = {'users_list': []}
    for user in users['users_list']:
        if user['name'] == name:
            subdict['users_list'].append(user)
    return subdict


users = {
    'users_list':
    [
        {
            'id': 'xyz789',
            'name': 'Charlie',
            'job': 'Janitor',
        },
        {
            'id': 'abc123',
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id': 'ppp222',
            'name': 'Mac',
            'job': 'Professor',
        },
        {
            'id': 'yat999',
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id': 'zap555',
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}
