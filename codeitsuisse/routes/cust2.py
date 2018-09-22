import math
import logging
from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/customers-and-hotel/minimum-camps', methods=['POST','GET'])
def evaluate_minimum_camps():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    custs = data;
    print(custs)
    lst = []
    for x in custs:
        pos = x["pos"]
        dist = x["distance"]
        lst.append([pos, dist])
    sorted_lst = sorted(lst)
    def checker(lst, ind, nxtind):
        if ind == len(lst):
            return 0
        if nxtind >= len(lst):
            return 1
        if lst[ind][0] + lst[ind][1] + lst[nxtind][1] >= lst[nxtind][0]:
            return checker(lst, ind, nxtind + 1)
        elif lst[ind][0] + lst[ind][1] + lst[nxtind][1] < lst[nxtind][0]:
            return 1 + checker(lst, nxtind, nxtind+1)
        else:
            return 1 + checker(lst, nxtind, nxtind+1)
    result = {'answer':checker(sorted_lst, 0, 1)}
    print(result)
    logging.info("My result :{}".format(result))
    return jsonify(result);