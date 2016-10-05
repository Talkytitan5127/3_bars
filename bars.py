import json
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "rb") as file_handler:
        return json.loads(file_handler.read().decode('utf-8'))


def get_biggest_bar(data):
    quantity_of_seats=data[0]["Cells"]["SeatsCount"]
    name_of_bar=data[0]["Cells"]["Name"]
    for bar in data:
        if bar["Cells"]["SeatsCount"]>quantity_of_seats:
            name_of_bar=bar["Cells"]["Name"]
            quantity_of_seats=bar["Cells"]["SeatsCount"]
    return name_of_bar


def get_smallest_bar(data):
    quantity_of_seats=data[0]["Cells"]["SeatsCount"]
    name_of_bar=data[0]["Cells"]["Name"]
    for bar in data:
        if bar["Cells"]["SeatsCount"]<quantity_of_seats:
            name_of_bar=bar["Cells"]["Name"]
            quantity_of_seats=bar["Cells"]["SeatsCount"]
    return name_of_bar


def get_closest_bar(data,longitude,latitude):
    distance=2e16
    name_of_bar=None
    for bar in data:
        bar_longitude=bar["Cells"]["geoData"]["coordinates"][0]
        bar_latitude=bar["Cells"]["geoData"]["coordinates"][1]
        length=((bar_longitude-longitude)**2+(bar_latitude-latitude)**2)**0.5
        if length<distance:
            name_of_bar=bar["Cells"]["Name"]
            distance=length
    return name_of_bar 
    
    
if __name__ == '__main__':
    print("Enter the path to the file")
    file=load_data(input())
    print("Enter longitude,latitude")
    longitude,latitude=map(float,input().split())
    print("The biggest bar is",get_biggest_bar(file),sep='-')
    print("The smallest bar is",get_smallest_bar(file),sep='-')
    print("The closest bar is",get_closest_bar(file,longitude,latitude),sep='-')
    
