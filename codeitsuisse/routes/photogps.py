# from flask import Flask
# from flask import request, jsonify
# import json
# from codeitsuisse import app;
#
# app = Flask(__name__)
#
# @app.route('/imagesGPS', methods=['POST'])
# def upload_file():
#
# 	# content = request.get_json()
# 	content = request.get_json()
# 	print('hi')
# 	print (content)
# 	# TODO : remember to add in the method
# 	return jsonify(main(content))
#
#
#
# # @app.route('/square', methods=['POST'])
# # def evaluate():
# #     data = request.get_json();
# #     logging.info("data sent for evaluation {}".format(data))
# #     inputValue = data.get("input");
# #     result = inputValue * inputValue
# #     logging.info("My result :{}".format(result))
# #     return jsonify(result);
#
# def main():
#
# 	# for i in images_path:
#
# 	# 	print (i["path"]);
#
# 	# with open('images_path.json') as f:
# 	# 	data = json.load(f)
#
# 	# image = Image.open("IMG_7055.jpg")
# 	# info = image._getexif()
#
# 	# for tag, value in info.items():
# 	# 	key = TAGS.get(tag, tag)
#
# 	# 	if key == "SubjectLocation":
# 	# 		print(key + " " + str(value))
#
# 		# print(key + " " + str(value))
#
# 	image = Image.open("IMG_7175.jpg")
# 	exif_data = get_exif_data(image)
# 	print (exif_data)
#
# 	return get_lat_lon(exif_data)
#
# def get_exif_data(image):
#     """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
#     exif_data = {}
#
# 	# try:
#     info = image._getexif()
#     if info:
#         for tag, value in info.items():
#         	decoded = TAGS.get(tag, tag)
#         if decoded == "GPSInfo":
#             gps_data = {}
#             for t in value:
#                 sub_decoded = GPSTAGS.get(t, t)
#                 gps_data[sub_decoded] = value[t]
#
#             exif_data[decoded] = gps_data
#         else:
#             exif_data[decoded] = value
#
#     return exif_data
#
#
# def get_if_exist(data, key):
# 	if key in data:
# 		return data[key]
#
# 	return None
#
# def _convert_to_degress(value):
#     """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
#     d0 = value[0][0]
#     d1 = value[0][1]
#     d = float(d0) / float(d1)
#
#     m0 = value[1][0]
#     m1 = value[1][1]
#     m = float(m0) / float(m1)
#
#     s0 = value[2][0]
#     s1 = value[2][1]
#     s = float(s0) / float(s1)
#
#     return d + (m / 60.0) + (s / 3600.0)
#
# def get_lat_lon(exif_data):
#     """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
#     lat = None
#     lon = None
#
#     if "GPSInfo" in exif_data:
#         gps_info = exif_data["GPSInfo"]
#
#         gps_latitude = get_if_exist(gps_info, "GPSLatitude")
#         gps_latitude_ref = get_if_exist(gps_info, 'GPSLatitudeRef')
#         gps_longitude = get_if_exist(gps_info, 'GPSLongitude')
#         gps_longitude_ref = get_if_exist(gps_info, 'GPSLongitudeRef')
#
#         if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
#             lat = _convert_to_degress(gps_latitude)
#             if gps_latitude_ref != "N":
#                 lat = 0 - lat
#
#             lon = _convert_to_degress(gps_longitude)
#             if gps_longitude_ref != "E":
#                 lon = 0 - lon
#
#     return lat, lon
#
#
#
#
# if __name__ == '__main__':
# 	app.run(debug=True)
#
#
#
