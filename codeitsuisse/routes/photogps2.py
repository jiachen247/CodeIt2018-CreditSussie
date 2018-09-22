from GPSPhoto import gpsphoto
import exifread
import logging

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)
@app.route('/imagesGPS', methods=['POST','GET'])
def evaluate_imagesGPS():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    pathlist = data.get();
    # pathlist = [{'path': "https://cis2018-photo-gps.herokuapp.com/images/sample1.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/sample2.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/sample3.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/sample4.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/sample5.jpg"}]  
    lst = []
    for x in pathlist:
        url = x['path']
        data = gpsphoto.getRawData(url)
        lst.append(data[tag])
    result = lst
    print(result)
    logging.info("My result :{}".format(result))
    return jsonify(result);