import logging
from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/customers-and-hotel/minimum-distance', methods=['POST','GET'])
def evaluate_minimum_distance():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    custs = data;
    custs_sorted = custs.sort()
    max_d = 0
    for x in range(len(custs)):
        if abs(custs_sorted[x] - custs_sorted[x-1]) > max_d:
            max_d = abs(custs_sorted[x] - custs_sorted[x-1])
        elif abs(custs_sorted[x] - custs_sorted[x+1]) > max_d:
            max_d = abs(custs_sorted[x] - custs_sorted[x+1])
    result = {"answer": max_d}
    logging.info("My result :{}".format(result))
    print(result)
    return jsonify(result);