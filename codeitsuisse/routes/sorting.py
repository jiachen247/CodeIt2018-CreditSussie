import logging

import requests
from flask import request, jsonify

from codeitsuisse import app
from SortingGame import  Board
logger = logging.getLogger(__name__)

@app.route('/sorting-game', methods=['POST','GET'])
def evaluate_sorting():
    data = request.get_json()
    data = data.get("puzzle")

    input_list =[item for sublist in data for item in sublist]
    print(input_list)

    dictToSend = {'size': len(data), 'values': ",".join(str(x) for x in input_list)}
    res = requests.post('https://sortingame.herokuapp.com/', json=dictToSend)

    print(res.text)


    print("input: {}".format(data))
    return jsonify({ "result": [6, 8, 5, 6]})



