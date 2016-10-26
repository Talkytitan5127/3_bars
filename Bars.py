import os
import json
from length_of_gpsline import get_length_between_coordinates


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    the_biggest_bar = max(data, key=lambda bars: bars["Cells"]["SeatsCount"])
    return the_biggest_bar["Cells"]["Name"], the_biggest_bar["Cells"]["SeatsCount"]


def get_smallest_bar(data):
    the_smallest_bar = min(data, key=lambda bars: bars["Cells"]["SeatsCount"])
    return the_smallest_bar["Cells"]["Name"], the_smallest_bar["Cells"]["SeatsCount"]


def get_nearest_bar(data, latitude, longitude):
    distance_to_nearest_bar = 2e16
    name_of_nearest_bar = 'None'
    for bar in data:
        bar_latitude = bar["Cells"]["geoData"]["coordinates"][0]
        bar_longitude = bar["Cells"]["geoData"]["coordinates"][1]
        distance_to_bar = get_length_between_coordinates(latitude, longitude, bar_latitude, bar_longitude)
        if distance_to_bar < distance_to_nearest_bar:
            distance_to_nearest_bar = distance_to_bar
            name_of_nearest_bar = bar["Cells"]["Name"]
    return name_of_nearest_bar, distance_to_nearest_bar


if __name__ == '__main__':
    file = load_data('Bars.json')
    the_biggest_bar, amount_of_seats = get_biggest_bar(file)
    print("The biggest bar is \"{}\". Amount of seats is {}".format(the_biggest_bar, amount_of_seats))
    the_smallest_bar, amount_of_seats = get_smallest_bar(file)
    print("The smallest bar is \"{}\". Amount of seats is {}".format(the_smallest_bar, amount_of_seats))
    latitude, longitude = map(float, input("Enter latitude, longitude of your location:").split())
    the_nearest_bar, distance_to_bar = get_nearest_bar(file, latitude, longitude)
    print("The nearest bar is \"{}\".".format(the_nearest_bar))
