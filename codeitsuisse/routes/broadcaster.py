import logging
from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/broadcaster/message-broadcast', methods=['POST','GET'])

def evaluate_broadcaster():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    node_list = data.get("data");
    broadcast = [[],[]]
    for x in node_list:
        if x[0] in broadcast[1]:
            broadcast[1].append(x[0])
        else:
            broadcast[0].append(x[0])
        broadcast[1].append(x[-1])
    first = broadcast[0]
    second = broadcast[1]
    newlist = []
    for i in first:
        if i not in newlist:
            newlist.append(i)
    result = newlist
    print(result)
    logging.info("My result :{}".format(result))
    return jsonify(result);