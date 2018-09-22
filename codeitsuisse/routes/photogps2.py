import exifread as ef
from flask import request, jsonify, logging
from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/imagesGPS', methods=['POST','GET'])
def evaluate_imagesGPS():
    print("sueijiksjkcbdkcnjsdnc")
    data = request.get_json();
    print(data)
    logging.info("data sent for evaluation {}".format(data))
    pathlist = data.get()
    print('Input:', pathlist)
    # pathlist = [{'path': "https://cis2018-photo-gps.herokuapp.com/images/sample1.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/sample2.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/sample3.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/sample4.jpg"},
    # {'path': "https://cis2018-photo-gps.herokuapp.com/images/sample5.jpg"}] 
    def _convert_to_degress(value):
        """
        Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
        :param value:
        :type value: exifread.utils.Ratio
        :rtype: float
        """
        d = float(value.values[0].num) / float(value.values[0].den)
        m = float(value.values[1].num) / float(value.values[1].den)
        s = float(value.values[2].num) / float(value.values[2].den)

        return d + (m / 60.0) + (s / 3600.0)
    def getGPS(filepath):
        '''
        returns gps data if present other wise returns empty dictionary
        '''
        with open(filepath, 'r') as f:
            tags = ef.process_file(f)
            latitude = tags.get('GPS GPSLatitude')
            latitude_ref = tags.get('GPS GPSLatitudeRef')
            longitude = tags.get('GPS GPSLongitude')
            longitude_ref = tags.get('GPS GPSLongitudeRef')
            if latitude:
                lat_value = _convert_to_degress(latitude)
                if latitude_ref.values != 'N':
                    lat_value = -lat_value
            else:
                return {}
            if longitude:
                lon_value = _convert_to_degress(longitude)
                if longitude_ref.values != 'E':
                    lon_value = -lon_value
            else:
                return {}
            return {'latitude': lat_value, 'longitude': lon_value}
        return {} 
    lst = []
    for x in pathlist:
        filepath = x['path']
        gps = getGPS(filepath)
        print(gps)
        lst.append(gps)
    print(lst)
    result = lst
    logging.info("My result :{}".format(result))
    return jsonify(result)
# evaluate_imagesGPS()






