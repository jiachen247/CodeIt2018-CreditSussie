import logging
import operator

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/tally-expense', methods=['POST','GET'])
def evaluate_tally_expense():
    data = request.get_json();
    print("input: {}".format(data))
    logging.info("data sent for evaluation {}".format(data))
    list_of_persons = data.get("persons");
    tally = {}
    for x in list_of_persons:
        tally[x] = 0
    expenses = data.get("expenses");
    for x in expenses:
        amount = x.get("amount")
        paidBy = x.get("paidBy")
        exclude = x.get("exclude")
        if isinstance(exclude, list):
            payable = [a for a in list_of_persons if (not a in exclude)]
        else:
            payable = [a for a in list_of_persons if not a == exclude]
        eachpay = amount/len(payable)
        for x in payable:
            tally[x] += eachpay
        tally[paidBy] -= amount
        balancer = {"transactions": []}
    while sorted(tally.items(), key=operator.itemgetter(1),reverse=True)[0][1]>0.0001:
        sorted_tally = sorted(tally.items(), key=operator.itemgetter(1),reverse=True)
        balances = {}
        diff_highest_lowest = sorted_tally[0][1] + sorted_tally[-1][1] 
        if diff_highest_lowest > 0: 
            balances["from"] = sorted_tally[0][0]
            balances["to"] = sorted_tally[-1][0]
            balances["amount"] = round(abs(sorted_tally[-1][1]), 2)
            tally[sorted_tally[-1][0]] = 0 
            tally[sorted_tally[0][0]] = diff_highest_lowest 
        else:  
            balances["from"] = sorted_tally[0][0] 
            balances["to"] = sorted_tally[-1][0]
            balances["amount"] = round(abs(sorted_tally[0][1]), 2)
            tally[sorted_tally[-1][0]] = diff_highest_lowest 
            tally[sorted_tally[0][0]] = 0
        balancer["transactions"].append(balances)
    result = balancer
    logging.info("My result :{}".format(result))
    print("output: {}".format(result))
    return jsonify(result);