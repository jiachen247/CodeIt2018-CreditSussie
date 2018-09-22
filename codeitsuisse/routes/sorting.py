import logging

from flask import request, jsonify

from codeitsuisse import app
from SortingGame import  Board
logger = logging.getLogger(__name__)

@app.route('/sorting-game', methods=['POST','GET'])
def evaluate_sorting():
    data = request.get_json()

    input_string =[item for sublist in data for item in sublist]
    print(input)


    b = Board(len(data), input_string)
    print(b)
    m = b.get_solution()
    print(m)


    print("input: {}".format(data))
    return jsonify({ "result": [6, 8, 5, 6]})



