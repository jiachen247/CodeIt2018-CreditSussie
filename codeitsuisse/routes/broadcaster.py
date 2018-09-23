import logging
from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/broadcaster/message-broadcast', methods=['POST','GET'])
def evaluate_broadcaster():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    node_list = data.get("data");
    print("Input Data:", node_list)
    broadcast = [[],[]]
    for x in node_list:
        (a, b) = x.split('->')
        if a in broadcast[1]:
            broadcast[1].append(a)
        else:
            broadcast[0].append(a)
        broadcast[1].append(b)
    first = broadcast[0]
    second = broadcast[1]
    newlist = []
    for i in first:
        if (i not in newlist) and (i not in second):
            newlist.append(i)
    result = {"result": newlist}
    print("Output Data:", result)
    logging.info("My result :{}".format(result))
    return jsonify(result);