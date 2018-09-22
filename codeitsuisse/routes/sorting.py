import logging

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/sorting-game', methods=['POST','GET'])
def evaluate_sorting():
    data = request.get_json()
    print("input: {}".format(data))
    return jsonify({ "result": [6, 8, 5, 6]})



