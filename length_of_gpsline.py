from math import pi
from math import sin
from math import cos
from math import atan2
from math import sqrt


def get_length_between_coordinates(latitude_1, longitude_1, latitude_2, longitude_2):
    earth_radius = 6372795
    # coordinates turn in radians

    latitude_1 *= pi/180
    longitude_1 *= pi/180
    latitude_2 *= pi/180
    longitude_2 *= pi/180

    # cos and sin of latitude and difference between longitude

    cos_lat_1 = cos(latitude_1)
    sin_lat_1 = sin(latitude_1)
    cos_lat_2 = cos(latitude_2)
    sin_lat_2 = sin(latitude_2)
    delta = longitude_2 - longitude_1
    cos_delta = cos(delta)
    sin_delta = sin(delta)

    # scaling length of bigger round

    coordinate_y = sqrt(pow(cos_lat_2*sin_delta, 2)+pow(cos_lat_1*sin_lat_2-sin_lat_1*cos_lat_2*cos_delta, 2))
    coordinate_x = sin_lat_1*sin_lat_2+cos_lat_1*cos_lat_2*cos_delta
    tan = atan2(coordinate_y, coordinate_x)
    distance = tan*earth_radius
    return distance
