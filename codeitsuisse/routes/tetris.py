import logging
import random
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/tetris', methods=['POST','GET'])
def evaluate_tetris():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    x = data.get();
    tetros = x["tetrominoSequence"]
    print(tetros)
    seq = []
    for x in range(len(tetros)):
        right = str(random.randint(0,8))
        turn = str(random.randint(0,3))
        seq.append(turn+right)
    result = {"actions": seq}
    logging.info("My result :{}".format(result))
    return jsonify(result);