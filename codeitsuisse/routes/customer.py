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
    print(custs)
    max_d = 0
    for x in range(len(custs)):
        overflow_val = abs(custs[-1] - custs[0]) - 1
        overflow_index = len(custs)
        y = x + 1
        if y >= overflow_index:
            y = y - overflow_index
        if x == 0:
            if abs(custs[x] - custs[x-1]) - overflow_val <= abs(custs[x] - custs[y]):
                if abs(custs[x] - custs[x-1]) - overflow_val > max_d:
                    max_d = abs(custs[x] - custs[x-1]) - overflow_val
            else:
                if abs(custs[x] - custs[y]) > max_d:
                    max_d = abs(custs[x] - custs[y])
        elif x == overflow_index - 1:
            if abs(custs[x] - custs[x-1]) <= abs(custs[x] - custs[y]) - overflow_val:
                if abs(custs[x] - custs[x-1]) > max_d:
                    max_d = abs(custs[x] - custs[x-1])
            else:
                if abs(custs[x] - custs[y]) - overflow_val > max_d:
                    max_d = abs(custs[x] - custs[y]) - overflow_val
        else:
            if abs(custs[x] - custs[x-1]) <= abs(custs[x] - custs[y]):
                if abs(custs[x] - custs[x-1]) > max_d:
                    max_d = abs(custs[x] - custs[x-1])
            else:
                if abs(custs[x] - custs[y]) > max_d:
                    max_d = abs(custs[x] - custs[y])

        result = {"answer": max_d}
    result["answer"] = math.ceil(max_d/2)
    logging.info("My result :{}".format(result))
    return jsonify(result);