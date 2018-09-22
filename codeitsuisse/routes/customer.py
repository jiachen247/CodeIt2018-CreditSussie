import math
import logging
from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/customers-and-hotel/minimum-distance', methods=['POST','GET'])
def evaluate_minimum_distance():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    custs = data;
    custs.sort()
    for x in range(len(custs)):
        overflow_val = abs(custs[-1] - custs[0]) - 1
        overflow_index = len(custs)
        y = x + 1
        if x == 0:
            counter = abs(custs[x] - custs[y])
        if y >= overflow_index:
            break
        if abs(custs[x] - custs[y]) < counter:
            counter = abs(custs[x] - custs[y])
    result = {"answer": counter}
    print(result)
    logging.info("My result :{}".format(result))
    return jsonify(result);