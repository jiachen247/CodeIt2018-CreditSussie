import logging

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/prime-sum', methods=['POST','GET'])
def evaluate_prime_sum():
    print('test')
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
    lst = []
    for x in range(2, inputValue + 1):
        if is_prime(x):
            lst.append(x)
    def helper(n, lst, primes):
        if n < 0:
            return None
        elif n == 0:
            return primes
        elif len(lst) == 0:
            return None
        else:
            x = lst[0]
            primecopy = primes[:]
            primecopy.append(lst[0])
            primelst.append(helper(n - x, lst[1:], primecopy))
            primelst.append(helper(n, lst[1:], primes))     
    primelst = []
    helper(inputValue, lst, primelst)
    def func(lst):
        z = []
        for x in lst:
            if isinstance(x, list):
                z.append(func(x))
            elif x != None:
                z.append(x)
        return z
    result = func(primelst)[0]
    result.reverse()
    logging.info("My result :{}".format(result))
    print(result)
    return jsonify(result);