import logging

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/test', methods=['POST','GET'])
def evaluate_test():
    return jsonify({"test":"testtttt"})



