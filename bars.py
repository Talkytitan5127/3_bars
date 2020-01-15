import argparse
import json
import os

from math import sqrt


def get_distance_between_coordinates(person_coordinates, bar_coordinates):
    person_latitude, person_longitude = person_coordinates
    bar_latitude, bar_longitude = bar_coordinates

    latitude_difference = (person_latitude - bar_latitude)**2
    longitude_difference = (person_longitude - bar_longitude)**2
    distance = sqrt(latitude_difference + longitude_difference)
    return distance


def load_data_from_file(filepath):
    if not os.path.exists(filepath):
        raise FileExistsError('File doesn"t exist')
    try:
        with open(filepath, 'r') as file_handler:
            return json.load(file_handler)
    except json.JSONDecodeError:
        return None


def get_biggest_bar(bars_data):
    biggest_bar = max(
        bars_data,
        key=lambda bars: bars['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bars_data):
    smallest_bar = min(
        bars_data,
        key=lambda bars: bars['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(bars_data, coordinates):
    closest_bar = min(bars_data,
                      key=lambda bars: get_distance_between_coordinates(
                                        coordinates,
                                        bars['geometry']['coordinates']
                                        )
                      )
    return closest_bar


def get_bar_phone(info_about_bar):
    public_phone = info_about_bar['PublicPhone'].pop()
    return public_phone['PublicPhone']


def get_numeric_location(location):
    try:
        return [float(number) for number in location]
    except ValueError:
        return None
    except TypeError:
        return None


def print_info_about_bar(bar, search_criteria):
    info_about_bar = bar['properties']['Attributes']
    bar_name = info_about_bar['Name']
    bar_address = info_about_bar['Address']
    bar_seat_count = info_about_bar['SeatsCount']
    bar_phone = get_bar_phone(info_about_bar)

    print_string = """
The {criteria} bar is {name}.
You can find it at: {address},
Telephone: {phone},
'Seats count: {count}.
"""
    print(print_string.format(
        criteria=search_criteria,
        name=bar_name,
        address=bar_address,
        phone=bar_phone,
        count=bar_seat_count
    ))


def create_argparser():
    argparser = argparse.ArgumentParser(description='Moscow bars')
    argparser.add_argument('-b', help='get info about the biggest bar',
                           action='store_true')
    argparser.add_argument('-s', help='get info about the smallest bar',
                           action='store_true')
    argparser.add_argument('--location',
                           help='get the nearest bar to your location',
                           type=str, dest='location', action='store', nargs=2,
                           metavar=('LATITUDE', 'LONGITUDE'))
    argparser.add_argument('--filepath',
                           help='path to file with bars in json format',
                           type=str, dest='filepath', default='bars.json')
    return argparser


if __name__ == '__main__':
    argparser = create_argparser()
    args = argparser.parse_args()

    bars_data = load_data_from_file(args.filepath)
    if bars_data is None:
        exit('Invalid format file (maybe it"s not json)')

    bars = bars_data['features']

    if args.b:
        print_info_about_bar(get_biggest_bar(bars), 'biggest')

    if args.s:
        print_info_about_bar(get_smallest_bar(bars), 'smallest')

    coordinates = get_numeric_location(args.location)
    if coordinates is None:
        exit('smth wrong with geo location')

    print_info_about_bar(get_closest_bar(bars, coordinates), 'nearest')
