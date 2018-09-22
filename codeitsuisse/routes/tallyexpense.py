import logging

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/tally-expense', methods=['POST','GET'])
def evaluate():
    data = request.get_json();
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
        if ifinstance(exclude, list):
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
        diff_highest_lowest = sorted_tally[0][1] + sorted_tally[-1][1] # Note that array[-1] is the last element of an array (for us: lowest value)
        if diff_highest_lowest > 0: # In this case the lowest amount can't fill the highest amount
            balances["from"] = sorted_tally[-1][0]
            balances["to"] = sorted_tally[0][0]
            balances["amount"] = abs(sorted_tally[-1][1])
            tally[sorted_tally[-1][0]] = 0 # The lowest bill is done paying!
            tally[sorted_tally[0][0]] = diff_highest_lowest # The person with the most amount of money still needs to receive money
        else: # The highest amount gets completely paid off. 
            balances["from"] = sorted_tally[-1][0]
            balances["to"] = sorted_tally[0][0]
            balances["amount"] = abs(sorted_tally[0][1])
            tally[sorted_tally[-1][0]] = diff_highest_lowest # The lowest person still has to pay
            tally[sorted_tally[0][0]] = 0 # The richest person got all of his money
        balancer["transactions"].append(balances)
    result = balancer
    logging.info("My result :{}".format(result))
    return jsonify(result);