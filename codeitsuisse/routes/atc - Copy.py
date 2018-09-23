# import logging
# import math
# from flask import request, jsonify;

# # from codeitsuisse import app;

# # logger = logging.getLogger(__name__)
# # @app.route('/airtrafficcontroller', methods=['POST','GET'])
# def evaluate_airtrafficcontroller():
#     # data = request.get_json()
#     # logging.info("data sent for evaluation {}".format(data))
#     data = {
#     "Flights": [
#         {
#             "PlaneId": "TR123",
#             "Time": "0200"
#         },
#         {
#             "PlaneId": "SQ255",
#             "Time": "0210"
#         },
#         {
#             "PlaneId": "TH544",
#             "Time": "0155"
#         },
#         {
#             "PlaneId": "BA123",
#             "Time": "0212"
#         },
#         {
#             "PlaneId": "VA521",
#             "Time": "0230"
#         }
#     ],
#     "Static": {
#         "Runways": ["A", "B"],
#         "ReserveTime": "600"
#     }
# }
#     lof = data.get("Flights")
#     secs = data.get("Static")
#     seconds = int(secs["ReserveTime"])

#     mins = (seconds/60)
#     flight_list = []
#     for x in lof:
#         time = x["Time"]
#         minss = int(time[0:2])*60 + int(time[2:4])
#         num = x["PlaneId"]
#         flight_list.append([minss, num])
#     flight_list.sort()
#     if 'Runways' in secs.keys():
#         runways = secs["Runways"]
#         rw_lst = []
#         for x in sorted(runways, reverse=True):
#             rw_lst.append([x, 0])
#         cur = len(rw_lst) - 1
#         print(rw_lst)
#         for x in range(len(flight_list)):
#             if x == 0:
#                 flight_list[x].append(rw_lst[cur][0])
#                 rw_lst[cur][1] = flight_list[x][0]
#                 cur -= 1
#             else:
#                 if cur < -len(rw_lst):
#                     cur += len(rw_lst)
#                 flight_list[x].append(rw_lst[cur][0])
#                 if flight_list[x][0] - rw_lst[cur][1] < mins:
#                     flight_list[x][0] += int(mins - (flight_list[x][0] - rw_lst[cur][1]))
#                     rw_lst[cur][1] = flight_list[x][0]
#                 cur -=1
#     else:
#         for x in range(len(flight_list)-1):
#             first_ft = flight_list[x][0]
#             second_ft = flight_list[x+1][0]
#             if second_ft - first_ft < mins:
#                 flight_list[x+1][0] += int(mins - (second_ft - first_ft))
#     final = []
#     for x in flight_list:
#         dic = {}
#         dic["PlaneId"] = x[1]
#         h = str(x[0] // 60).zfill(2)
#         m = str(x[0] % 60).zfill(2)
#         dic["Time"] = h+m
#         if secs["ReserveTime"]:
#             dic["Runway"] = x[2]
#         final.append(dic)
#     result = {"Flights": final}
#     print(result)
#     # logging.info("My result :{}".format(result))
#     # return jsonify(result)
# evaluate_airtrafficcontroller()