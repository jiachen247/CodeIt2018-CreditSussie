import logging
from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/customers-and-hotel/minimum-distance', methods=['POST','GET'])
def evaluate_minimum_distance():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    custs = data.get("input");
    max_d = 0
    for x in range(len(custs)):
        if abs(custs.sorted()[x] - custs.sorted()[x-1]) > max_d:
            max_d = abs(custs.sorted()[x] - custs.sorted()[x-1])
        elif abs(custs.sorted()[x] - custs.sorted()[x+1]) > max_d:
            max_d = abs(custs.sorted()[x] - custs.sorted()[x+1])
    result = {"answer": max_d}
    logging.info("My result :{}".format(result))
    print(result)
    return jsonify(result);