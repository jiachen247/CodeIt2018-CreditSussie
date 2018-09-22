# import logging

# from flask import request, jsonify;

# from codeitsuisse import app;

# logger = logging.getLogger(__name__)

# @app.route('/square', methods=['POST','GET'])
# def evaluate():
#     data = request.get_json();
#     logging.info("data sent for evaluation {}".format(data))
#     inputValue = data.get("input");
#     def is_prime(num):
#     if num > 1:
#        # check for factors
#        for i in range(2,num):
#            if (num % i) == 0:
#                 return False
#        else:
#            return True
#     def helper():
#         lst = []
#         for x in range(2, inputValue):
#             if is_prime(x):
#                 lst.append(x)
#         return lst
#     list_of_primes = helper()
#     def helper2(n, lst, primes):
#         if n == 0:
#             return primes
#         elif n <= 0:
#             break
#         else: 
#             return [helper2(n, lst.remove(n), primes.append(n)), + helper2(n-lst[0], lst.remove(n), primes.append(n))]
#     result = helper2(inputValue, list_of_primes, [])
#     logging.info("My result :{}".format(result))
#     return jsonify(result);


def evaluate():
    inputValue = 19
    
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

    # 
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
    z = []
    def func(lst):
        for x in lst:
            if isinstance(x, list):
                func(x)
            elif x != None:
                z.append(x)
    func(primelst)
    print(primelst)
    print(z)
evaluate()