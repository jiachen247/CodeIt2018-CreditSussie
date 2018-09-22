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
    size = len(data)

    input_list =[item for sublist in data for item in sublist]
    print(input_list)

    dictToSend = {'size': size, 'values': ",".join(str(x) for x in input_list)}
    res = requests.post('https://sortingame.herokuapp.com/', json=dictToSend)

    moves = res.json()
    results = []

    def find_zero(p):
        for x in range(size):
            for y in range(size):
                if p[x][y] == 0:
                    return [x, y]

        print("[+] zero not found.")
        return [-1, -1]

    def swap_moves(p, target):
        z = find_zero(p)
        print("zero")
        print(z)
        print("target")
        print(target)
        p[z[0]][z[1]] = p[target[0]][target[1]]
        p[target[0]][target[1]] = 0
        return p[z[0]][z[1]]



    print("input: {}".format(data))

    for move in moves:
        print(move)
        results.append(swap_moves(data, move))
    return jsonify({ "result": results})



