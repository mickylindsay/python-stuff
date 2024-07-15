"""Parsing location-history.json from google maps timeline export"""

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

def parse_segment(data: Any):
    if "visit" in data:
        return parse_visit(data)
    if "activity" in data:
        return parse_activity(data)
    if "timelinePath" in data:
        return parse_path(data)
    return None

visits_within_bounds = []
# lat long bounding rect around Seattle
lat_min = 47.42
lat_max = 47.78
long_min = -122.44
long_max = -122.16

resolution = 100

lat_step = (lat_max - lat_min) / resolution
long_step = (long_max - long_min) / resolution

histogram = [0] * resolution * resolution

with open(os.path.dirname(__file__) + "/location-history.json", 'r') as content:
    location_data = json.load(content)['semanticSegments']
    for data in location_data:
        record = parse_segment(data)
        if record and lat_min < record.lat < lat_max and long_min < record.long < long_max:
            visits_within_bounds.append(record)
