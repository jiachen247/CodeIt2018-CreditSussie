import logging
import pandas as pd
import operator
from sklearn import linear_model
import requests
from flask import request, jsonify
from time import sleep

from codeitsuisse import app
logger = logging.getLogger(__name__)

@app.route('/machine-learning/question-2', methods=['POST'])
def evaluate_deeplearning2():
    data = request.get_json()
    question = data.get("question")
    print(len(question))

    answer = []
    for x in question:
        res = requests.post("https://tensorflow-mnist.herokuapp.com/api/mnist", json=x)
        r = res.json().get("results")[0]



        answer.append(max(r.iteritems(), key=operator.itemgetter(1))[0])
        sleep(0.1)


    print(answer)
    return jsonify({"answer": answer})



@app.route('/machine-learning/question-1', methods=['POST'])
def evaluate_deeplearning1():
    data = request.get_json()

    inputt = data.get("input")
    output = data.get("output")
    question = data.get("question")

    d = []
    index = 0

    for i in inputt:
        d.append({'x1': i[0], 'x2': i[1], 'x3': i[2], 'o': output[index]})
        index += 1

    # d = [{'x1': 1, 'x2': 2, 'x3': 3, 'o': 6},
    #          {'x1': 2, 'x2': 3, 'x3': 4, 'o': 9},
    #          {'x1': 2, 'x2': 1, 'x3': 4, 'o': 7},
    #          {'x1': 5, 'x2': 3, 'x3': 2, 'o': 10},
    #          {'x1': 2, 'x2': 1, 'x3': 2, 'o': 5}
    #          ]

    df = pd.DataFrame(d)

    reg = linear_model.LinearRegression()
    reg.fit(df[['x1', 'x2', 'x3']], df.o)
    prediction = reg.predict([question])[0]
    return jsonify({ "answer": prediction})




