#!/usr/bin/env python

# REST server
import json
import uuid
from os import abort
from random import sample

from flask import Flask, jsonify, request


app = Flask(__name__)

works = {}
works_done = {}


@app.route('/')
def index():
    return "Welcome to the Deco API-Rest!"


@app.route('/deco/api/get-work/<int:amount>', methods=['GET'])
def get_work(amount):
    if amount < 1:
        abort(400)

    if amount > len(works):
        amount = len(works)

    return jsonify([works[k] for k in sample(list(works.keys()), amount)])


@app.route('/deco/api/update-work/<id_work>', methods=['POST'])
def publish_result(id_work):
    if not request.json or 'result' not in request.json:
        abort(400)

    works[id_work]['result'] = request.json['result']

    works_done[id_work] = works[id_work]
    works_done[id_work]['reward'] = 50

    del works[id_work]

    return jsonify({'reward': 50}), 201


default_m1 = [[1, 0], [0, 1]]
default_m2 = [[0, 1], [1, 0]]


def turn_in_works(m1, m2):
    for a, b in zip(m1, m2):

        _id = str(uuid.uuid4())

        works[_id] = {
            "id": _id,
            "row": a,
            "col": b,
            "result": None
        }

        print("Work created: ", works[_id])


@app.route('/deco/api/transaction', methods=['POST'])
def publish_work():
    if not request.json:
        abort(400)

    data = json.loads(request.json)

    m1 = data.get('m1', default_m1)
    m2 = data.get('m2', default_m2)

    turn_in_works(m1, m2)

    return jsonify({"result": "ok"})


@app.route('/works')
def see_works():
    return jsonify(list(works.values()))


if __name__ == '__main__':
    app.run(debug=False, port=8080)
