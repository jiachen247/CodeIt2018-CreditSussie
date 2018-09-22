import logging
from flask import request, jsonify;
from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/broadcaster/fastest-path', methods=['POST','GET'])
def evaluate_fastest_path():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    node_list = data.get("data");
    sender = data.get("sender");
    recipient = data.get("recipient");
    broadcast = {}
    for x in node_list:
        (a, d) = x.split('->')
        (b, c) = d.split(',')
        if a in broadcast:
            broadcast[a][b] = c
        else:
            broadcast[a] = {}
            broadcast[a][b] = c
        if b not in broadcast:
            broadcast[b] = {}
    def get_length(letter):
        if "Updated" in broadcast[letter]:
            return broadcast[letter]["Updated"]
        for x in broadcast[letter]:
            if x == recipient:
                broadcast[letter]["Updated"] = broadcast[letter][x]
                return broadcast[letter][x]
        else:
            for x in broadcast[letter]:
                get_length(x)
    z = get_length(sender)
    result = {"result": z}
    print("Output Data:", result)
    logging.info("My result :{}".format(result))
    return jsonify(result);