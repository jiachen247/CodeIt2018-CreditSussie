import logging

import requests
from flask import request, jsonify

from codeitsuisse import app
from SortingGame import  Board
logger = logging.getLogger(__name__)



@app.route('/machine-learning/question-1', methods=['POST'])
def evaluate_deeplearning():
    data = request.get_data()
    print(data)
    return "hello"




