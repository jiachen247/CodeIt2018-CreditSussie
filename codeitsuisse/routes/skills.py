import logging

from flask import request, jsonify;

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/skill-tree', methods=['POST','GET'])
def evaluate_skill():
    data = request.get_json()
    print("in : {}".format(data))
    return jsonify({})



