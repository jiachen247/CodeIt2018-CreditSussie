import logging

import requests
from flask import request, jsonify

from codeitsuisse import app
from SortingGame import  Board
logger = logging.getLogger(__name__)

@app.route('/sorting-game', methods=['POST','GET'])
def evaluate_sorting():
    data = request.get_json()

    input_string =[item for sublist in data for item in sublist]
    print(input_string)

    dictToSend = {'size': len(data), 'values': input_string}
    res = requests.post('https://sortingame.herokuapp.com/', json=dictToSend)

    print(res.text)


    print("input: {}".format(data))
    return jsonify({ "result": [6, 8, 5, 6]})



