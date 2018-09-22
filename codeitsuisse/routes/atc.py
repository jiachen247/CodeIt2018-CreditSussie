import logging
import math
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/airtrafficcontroller', methods=['POST','GET'])
def evaluate_airtrafficcontroller():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    print('//////////////  INPUT ///////////////', data)

    lof = data.get("Flights")
    secs = data.get("Static")
    seconds = int(secs["ReserveTime"])

    mins = (seconds/60)
    flight_list = []
    dist = False
    hold = []
    for x in lof:
        time = x["Time"]
        minss = int(time[0:2])*60 + int(time[2:4])
        num = x["PlaneId"]
        if "Distressed" in x.keys():
            dist = True
            hold.append([minss, num, x["Distressed"]])
        else:
            flight_list.append([minss, num])
    flight_list.sort()
    if dist:
        flight_list.insert(0, hold[0][0:2])
    if 'Runways' in secs.keys():
        runways = secs["Runways"]
        rw_lst = []
        for x in runways:
            rw_lst.append([x, 0])
        cur = len(rw_lst) - 1
        for x in range(len(flight_list)):
            if x == 0:
                flight_list[x].append(rw_lst[cur][0])
                rw_lst[cur][1] = flight_list[x][0]
                cur -= 1
            else:
                if cur < -len(rw_lst):
                    cur += len(rw_lst)
                flight_list[x].append(rw_lst[cur][0])
                if flight_list[x][0] - rw_lst[cur][1] < mins:
                    flight_list[x][0] += int(mins - (flight_list[x][0] - rw_lst[cur][1]))
                    rw_lst[cur][1] = flight_list[x][0]
                cur -=1
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
        if 'Runways' in secs.keys():
            dic["Runway"] = x[2]
        final.append(dic)
    result = {"Flights": final}
    print(result)
    logging.info("My result :{}".format(result))
    return jsonify(result)
# evaluate_airtrafficcontroller()