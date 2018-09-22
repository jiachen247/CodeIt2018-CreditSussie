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
        d = d0 / d1
        m0 = value[1][0]
        m1 = value[1][1]
        m = m0 / m1
        s0 = value[2][0]
        s1 = value[2][1]
        s = s0 / s1
        return d + (m / 60) + (s / 3600)
    newlst = []
    for x in lst:
        lat = _convert_to_degress(x[2])
        lon = _convert_to_degress(x[4])
        newlst.append({"lat":lat,"lon":lon})
    result = newlst
    print(result)
    logging.info("My result :{}".format(result))
    return jsonify(result)
# evaluate_imagesGPS()






