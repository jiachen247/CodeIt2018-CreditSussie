import logging
import random
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/prime-sum', methods=['POST','GET'])
def evaluate_prime_sum():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    tetros = data.get("tetronimoSequence");
    seq = []
    for x in tetros:
        right = str(random.randint(0,8))
        turn = str(random.randint(0,3))
        seq.append(turn+right)
    result = {"actions": seq}
    logging.info("My result :{}".format(result))
    return jsonify(result);