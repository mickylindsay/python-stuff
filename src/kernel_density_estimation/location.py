"""Parsing location-history.json from google maps timeline export."""

import json
import os
import re
from typing import Any
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Visit:
    start_time : datetime
    endTime : datetime
    lat: float
    long: float

def convert_datetime(date_str: str) -> datetime:
    return datetime.fromisoformat(date_str)

def parse_visit(data: Any) -> Visit:
    start_time = convert_datetime(data["startTime"])
    end_time = convert_datetime(data["endTime"])
    lat_long = data["visit"]["topCandidate"]["placeLocation"]["latLng"]
    parsed = re.findall(r"-?\d+.\d+", lat_long)
    return Visit(start_time, end_time, float(parsed[0]), float(parsed[1]))

def parse_activity(data: Any):
    pass

def parse_path(data: Any):
    pass

def parse_activity_segment(data: Any):
    pass

def parse_place_visit(data: Any):
    location = data["placeVisit"]["location"]
    duration = data["placeVisit"]["duration"]
    start_time = convert_datetime(duration["startTimestamp"])
    end_time = convert_datetime(duration["endTimestamp"])
    lat = float(location["latitudeE7"]) / 10000000
    long = float(location["longitudeE7"]) / 10000000
    return Visit(start_time, end_time, lat, long)

def parse_segment(data: Any):
    if "visit" in data:
        return parse_visit(data)
    if "activity" in data:
        return parse_activity(data)
    if "timelinePath" in data:
        return parse_path(data)
    if "activitySegment" in data:
        return parse_activity_segment(data)
    if "placeVisit" in data:
        return parse_place_visit(data)
    return None

visits_within_bounds = []
# lat long bounding rect around Seattle
# lat_min = 47.42
# lat_max = 47.78
# long_min = -122.44
# long_max = -122.16

# lat long bounding rect around US
lat_min = 24.53
lat_max = 49.04
long_min = -125.08
long_max = -66.81

resolution = 100

lat_step = (lat_max - lat_min) / resolution
long_step = (long_max - long_min) / resolution

print(f"lat step: {lat_step} long step: {long_step}")

histogram = [0] * resolution * resolution

# semanticSegments only on new mobile timeline
# with open(os.path.dirname(__file__) + "/location-history.json", 'r') as content:
#     location_data = json.load(content)['semanticSegments']

# timelineObjects on old google takeout format
with open(os.path.dirname(__file__) + "/history/2024.json", 'r') as content:
    location_data = json.load(content)['timelineObjects']   
    for data in location_data:
        record = parse_segment(data)
        if record and lat_min < record.lat < lat_max and long_min < record.long < long_max:
            visits_within_bounds.append(record)
            lat_index = int((record.lat - lat_min) / lat_step)
            long_index = int((record.long - long_min) / long_step)
            histogram[lat_index * resolution + long_index] += 1
            print(f"time: {record.start_time} lat: {record.lat} long: {record.long} index: {lat_index} / {long_index}")

for y in range(resolution -1, 0, -1):
    for x in range(0, resolution):
        num = histogram[y * resolution + x]
        if num > 0:
            print(f"{num:02},", end="")
        else:
            print(f"  ,", end="")
    print()