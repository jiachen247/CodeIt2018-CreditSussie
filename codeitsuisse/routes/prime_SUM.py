import logging

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/prime-sum', methods=['POST','GET'])
def evaluate_prime_sum():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input");
    def is_prime(num):
        if num > 1:
       # check for factors
            for i in range(2, num):
               if (num % i) == 0:
                    return False
            return True
        else:
            return False
    pris = []
    def primer(inp):
        if is_prime(inp):
            pris.append(inp)
        elif is_prime(inp - 2):
            pris.append(inp - 2)
            pris.append(2)
        else:
            pris.append(3)
            primer(inp - 3)
    primer(inputValue)
    result = pris
    print(result)
    logging.info("My result :{}".format(result))
    return jsonify(result);
