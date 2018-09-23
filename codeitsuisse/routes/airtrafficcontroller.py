# import logging

# from flask import request, jsonify;

# from codeitsuisse import app;

# logger = logging.getLogger(__name__)

# @app.route('/airtrafficcontroller', methods=['POST','GET'])
# def evaluate():
#     data = request.get_json();
#     logging.info("data sent for evaluation {}".format(data))

#     list_of_flight_info = data.get("Flights");

#     planeID_list = []
#     time_list = []

#     for flight_dictionary in list_of_flight_info:
#     	planeID = flight_dictionary.get("PlaneId")
#     	time = flight_dictionary.get("Time")

# 		planeID_list.append(planeID)    
# 		time_list.append(time_list)

# 	# finds the earliest time
# 	earliest_time = min(float(s) for s in time_list)

# 	# returns index of earliest time 
# 	index_earliest_time = time_list.index(earliest_time)
# 	earliest_flight = planeID_list[index_earliest_time]

# 	# returns the rest of the list
# 	rest_of_time = del time_list[index_earliest_time]
# 	rest_of_flight = del planeID_list[index_earliest_time]

# 	first_flight = {"PlaneId": earliest_flight, "Time" : earliest_time }

# 	head_output_list = list(first_flight)
# 	tail_output_list = list()

# 	for x in rest_of_flight:

# 		dictionary = {}
# 		dictionary.update({"PlaneId": x})

# 			for y in rest_of_time:
# 				dictionary.update({"Time": y})
# 				tail_output_list.append(dictionary)

# 	result = head_output_list + tail_output_list
#     return jsonify(result);
	



