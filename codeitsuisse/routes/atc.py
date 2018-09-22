import logging
import math
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/airtrafficcontroller', methods=['POST','GET'])
def evaluate_airtrafficcontroller():
    data = request.get_json()
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
    if secs["ReserveTime"]:
        runways = secs["ReserveTime"]
        runway_A_time = 0
        runway_B_time = 0
        for x in range(0,len(flight_list),2):
            if x == 0:
                runway_A_time = flight_list[x][0]
                runway_B_time = flight_list[x+1][0]
                flight_list[x+1].append("B")
            else:
                if x != len(flight_list)-1:
                    if flight_list[x+1][0] - runway_B_time < mins:
                        flight_list[x+1][0] += int(mins - (flight_list[x+1][0] - runway_B_time))
                    flight_list[x+1].append("B")
                    runway_B_time = flight_list[x+1][0]
                if flight_list[x][0] - runway_A_time < mins:
                    flight_list[x][0] += int(mins - (flight_list[x+1][0] - runway_A_time))
                runway_A_time = flight_list[x][0]
            flight_list[x].append("A")
        print(flight_list)
    else:
        for x in range(len(flight_list)-1):
            first_ft = flight_list[x][0]
            second_ft = flight_list[x+1][0]
            if second_ft - first_ft < mins:
                flight_list[x+1][0] += int(mins - (second_ft - first_ft))
    final = []
    for x in flight_list:
        dic = {}
        dic["PlaneId"] = x[1]
        h = str(x[0] // 60).zfill(2)
        m = str(x[0] % 60).zfill(2)
        dic["Time"] = h+m
        if secs["ReserveTime"]:
            dic["Runway"] = x[2]
        final.append(dic)
    result = {"Flights": final}
    print(result)
    logging.info("My result :{}".format(result))
    return jsonify(result)
# evaluate_airtrafficcontroller()