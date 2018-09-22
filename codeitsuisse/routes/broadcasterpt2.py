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
    broadcast = {}
    for x in node_list:
        (a, b) = x.split('->')
        if a in broadcast:
            broadcast[a][0] += 1
        else:
            broadcast[a] = [1,b]
        if b not in broadcast:
            broadcast[b] = [0]
    def get_sum(letter):
        if broadcast[letter][-1] == 'Updated':
            return letter[0]
        else:
            for x in range(1, len(broadcast[letter]) - 1):
                broadcast[letter][0] += get_sum(x)
            broadcast[letter].append('Updated')
            return broadcast[letter][0]
    largest_val = 0
    letter = []
    for x in broadcast:
        val = get_sum(x)
        if val >= largest_val:
            largest_val = val
            letter.append([largest_val, x])
    letter.sort(reverse=True)
    best_letter = []
    for x in letter:
        if not x[0] == letter[0][0]:
            break
        else:
            best_letter.append(x[1])
    result = {"result": sorted(best_letter)[0]}
    print("Output Data:", result)
    logging.info("My result :{}".format(result))
    return jsonify(result);