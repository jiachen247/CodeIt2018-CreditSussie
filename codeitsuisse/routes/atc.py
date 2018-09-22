import logging
import math
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/airtrafficcontroller', methods=['POST','GET'])
def evaluate_airtrafficcontroller():
    data = request.get_json()
    print(data)
    logging.info("data sent for evaluation {}".format(data))
    lof = data.get("Flights")
    secs = data.get("Static")
    seconds = int(secs["ReserveTime"])
    mins = (seconds/60)
    flight_list = []
    for x in lof:
        time = x["Time"]
        minss = int(time[0:2])*60 + int(time[2:4])
        num = x["PlaneId"]
        flight_list.append([minss, num])
    flight_list.sort()
    print(flight_list)
    for x in range(len(flight_list)-1):
        first_ft = flight_list[x][0]
        second_ft = flight_list[x+1][0]
        if second_ft - first_ft < mins:
            flight_list[x+1][0] += int(mins - (second_ft - first_ft))
    final = []
    for x in flight_list:
        dic = {}
        dic["PlaneId"]=x[1]
        h = str(x[0] // 60).zfill(2)
        m = str(x[0] % 60).zfill(2)
        dic["Time"] = h+m
        print(dic)
        final.append(dic)
    result = {"Flights": final}
    print(result)
    logging.info("My result :{}".format(result))
    return jsonify(result)
# evaluate_airtrafficcontroller()