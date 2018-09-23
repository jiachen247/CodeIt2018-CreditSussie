import exifread as ef
from flask import request, jsonify
import logging
from codeitsuisse import app;
from PIL import Image, ExifTags
import requests
from io import BytesIO
logger = logging.getLogger(__name__)
@app.route('/imagesGPS', methods=['POST','GET'])
def evaluate_imagesGPS():
    data = request.get_json();
    print(data)
    logging.info("data sent for evaluation {}".format(data))
    # data = [{'path': "https://cis2018-photo-gps.herokuapp.com/images/zn5m.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/zn5m.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/zn5m.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/zn5m.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/zn5m.jpg"}]
    lst = []
    for x in data:
        filepath = x['path']
        response = requests.get(filepath)
        img = Image.open(BytesIO(response.content))
        exif = {ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in ExifTags.TAGS }
        lst.append(exif['GPSInfo'])
    print(lst)
    def _convert_to_degress(value):
        d0 = value[0][0]
        d1 = value[0][1]
        d = float(d0) / float(d1)
        m0 = value[1][0]
        m1 = value[1][1]
        m = float(m0) / float(m1)
        s0 = value[2][0]
        s1 = value[2][1]
        s = float(s0) / float(s1)
        return d + (m / 60.00) + (s / 3600.00)
    newlst = []
    for x in lst:
        lat = _convert_to_degress(x[2])
        if x[1] == "S":
            lat = -lat
        lon = _convert_to_degress(x[4])
        if x[3] == "W":
            lon = -lon
        newlst.append({"lat":lat,"long":lon})
    result = newlst
    print(result)
    logging.info("My result :{}".format(result))
    return jsonify(result)
# evaluate_imagesGPS()


# 2018-09-22T17:19:53.345328+00:00 app[web.1]: [{1: 'N', 2: ((65, 1), (12, 1), (6725, 4056)), 3: 'W', 4: ((46, 1), (11, 1), (33537, 800))}, {1: 'N', 2: ((19, 1), (8, 1), (39633, 1151)), 3: 'E', 4: ((72, 1), (56, 1), (42801, 1600))}, {1: 'N', 2: ((34, 1), (7, 1), (60001, 2454)), 3: 'E', 4: ((17, 1), (47, 1), (17463, 800))}, {1: 'N', 2: ((44, 1), (29, 1), (18067, 438)), 3: 'W', 4: ((107, 1), (49, 1), (39345, 5944))}, {1: 'N', 2: ((46, 1), (29, 1), (191687, 4105)), 3: 'E', 4: ((103, 1), (18, 1), (28480, 889))}]
# 2018-09-22T17:19:53.345738+00:00 app[web.1]: [{'lat': 65.20046056596537, 'lon': -46.194978125}, {'lat': 19.14289820445989, 'lon': 72.94076406250001}, {'lat': 34.12345841256905, 'lon': 17.789396875}, {'lat': 44.49479134956875, 'lon': -107.8185053555406}, {'lat': 46.49630443903099, 'lon': 103.30889888763905}]
# 2018-09-22T17:19:53.356079+00:00 app[web.1]: 10.30.70.204 - - [22/Sep/2018:17:19:53 +0000] "POST /imagesGPS HTTP/1.1" 200 245 "-" "axios/0.18.0"






