# from flask import Flask
# from flask import request, jsonify
# from codeitsuisse import app;
# import PIL 
# import json 
# from PIL import Image
# from PIL.ExifTags import TAGS, GPSTAGS 
# import urllib.request
# import logging

# # app = Flask(__name__)

# logger = logging.getLogger(__name__)

# @app.route('/imagesGPS', methods=['POST', 'GET'])
# def upload_file():
#     logging.info("data sent for evaluation {}".format(data))
#     content = request.get_json()
#     return jsonify(main(content))
# def main(content):
#     # loop through every image in the list of json 
#     lat_lon_list = []
#     n = 0
#     for every_image in content:
#         print (every_image)
#         n += 1
#     # if (every_image['path']):
#         image_url = every_image['path']            
#         # print (image_url)
#         urllib.request.urlretrieve(image_url, "{count}.jpg".format(count=n))
#         image = Image.open("{count}.jpg".format(count=n))
#         # get all the exif_data from each image
#         exif_data = get_exif_data(image)
#         lat, lon = get_lat_lon(exif_data)
#         lat_lon_list.append({"lat":lat, "lon": lon})
#         # else: 
#         #     print("second")
#     return lat_lon_list
# def get_exif_data(image):
#     """Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
#     global decoded
#     exif_data = {}
#     # try:
#     info = image._getexif()
#     if info:
#         for tag, value in info.items():
#             decoded = TAGS.get(tag, tag)
#         if decoded == "GPSInfo":
#             gps_data = {}
#             for t in value:
#                 sub_decoded = GPSTAGS.get(t, t)
#                 gps_data[sub_decoded] = value[t]

#             exif_data[decoded] = gps_data
#         else:
#             exif_data[decoded] = value
#     return exif_data
# def get_if_exist(data, key):
#     if key in data:
#         return data[key]
#     return None
# def _convert_to_degress(value):
#     """Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
#     d0 = value[0][0]
#     d1 = value[0][1]
#     d = float(d0) / float(d1)

#     m0 = value[1][0]
#     m1 = value[1][1]
#     m = float(m0) / float(m1)

#     s0 = value[2][0]
#     s1 = value[2][1]
#     s = float(s0) / float(s1)
#     return d + (m / 60.0) + (s / 3600.0)
# def get_lat_lon(exif_data):
#     print ("getting lat and lon")
#     """Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
#     lat = None
#     lon = None
#     if "GPSInfo" in exif_data:
#         gps_info = exif_data["GPSInfo"]

#         gps_latitude = get_if_exist(gps_info, "GPSLatitude")
#         gps_latitude_ref = get_if_exist(gps_info, 'GPSLatitudeRef')
#         gps_longitude = get_if_exist(gps_info, 'GPSLongitude')
#         gps_longitude_ref = get_if_exist(gps_info, 'GPSLongitudeRef')

#         if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
#             lat = _convert_to_degress(gps_latitude)
#             print ("converting lat to degrees")
#             if gps_latitude_ref != "N":
#                 lat = 0 - lat

#             lon = _convert_to_degress(gps_longitude)
#             print ("converting lon to degrees")

#             if gps_longitude_ref != "E":
#                 lon = 0 - lon
#     return lat, lon

# # if __name__ == '__main__':
# #     app.run(debug=True)



