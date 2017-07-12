import json
import os

from math import pi
from math import cos, sin
from math import sqrt, atan2

def get_length_distance(lat1, long1, lat2, long2):
    Radius = 6372795

    #translate coordinates to radians
    lat1 *= pi / 180
    long1 *= pi / 180
    lat2 *= pi / 180
    long2 *= pi / 180

    '''calculate cosinus and sinus of latitudes and
        difference longitudes'''
    cl1 = cos(lat1)
    cl2 = cos(lat2)
    sl1 = sin(lat1)
    sl2 = sin(lat2)

    delta = long2 - long1
    cdelta = cos(delta)
    sdelta = sin(delta)

    #calculate length of bigger round
    length_round_y = sqrt(pow(cl2 * sdelta, 2) + pow(cl1 * sl2 -
        sl1 * cl2 * cdelta, 2))
    length_round_x = sl1 * sl2 + cl1 * cl2 * cdelta
    ad = atan2(length_round_y, length_round_x)
    distance = ad * Radius
    return distance


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='UTF-8') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda bars: bars['Cells']['SeatsCount'])
    return biggest_bar

def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda bars: bars['Cells']['SeatsCount'])
    return smallest_bar


def get_closest_bar(data, latitude, longitude):
    closest_bar = min(data, key=lambda bars: get_length_distance(latitude, longitude,
        bars['Cells']['geoData']['coordinates'][1], bars['Cells']['geoData']['coordinates'][0]))
    return closest_bar


def pretty_print(data):
    print('The smallest bar is %s' % get_smallest_bar(data)['Cells']['Name'])
    print('The biggest bar is %s' % get_biggest_bar(data)['Cells']['Name'])


if __name__ == '__main__':
    filepath = input('Enter the path to the file \'bars.json\':')
    data = load_data(filepath)
    if not data:
        print('file can\'t be opened')
    else:
        pretty_print(data)

        latitude = float(input('Enter your coordinates\nlatitude:'))
        longitude = float(input('longitude:'))
        closest_bar = get_closest_bar(data, latitude, longitude)
        print('The closest bar is {}\nHis address is {}'.format(closest_bar['Cells']['Name'],
            closest_bar['Cells']['Address']))
