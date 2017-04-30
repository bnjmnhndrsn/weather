import django
import sys, os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hava.settings")
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), '..'))
django.setup()

import re
from django.contrib.gis.geos import GEOSGeometry
from decimal import Decimal
from weather.models import WeatherLocation

data = {}

def import_stations(filename):
    with open(filename) as f:
        for line in f.readlines():
            id = line[0:11]
            latitude = line[12:20]
            longitude = line[21:30]
            state = line[38:40]
            name = line[41:71]
            station_data = data.get(id, {})
            station_data.update({
                'id': id,
                'latitude': latitude.strip(),
                'longitude': longitude.strip(),
                'state': state,
                'station_name': name.strip()
            })
            data[id] = station_data

def import_zipcodes(filename):
    with open(filename) as f:
        for line in f.readlines():
            id = line[0:11]
            zipcode = line[12:17]
            name = line[18:]
            station_data = data.get(id, {})
            station_data.update({
                'zipcode': zipcode,
                'place_name': name.strip()
            })
            data[id] = station_data


def import_temperatures(filename, key):
    with open(filename) as f:
        regex = re.compile(' +')
        for line in f.readlines():
            split = regex.split(line)
            station = split[0]
            months = split[1:]
            months_formatted = []
            for month in months:
                stripped = month.strip()
                temperature = Decimal(stripped[:-1]) / Decimal(10)
                months_formatted.append({
                    'temperature': str(temperature)
                })
            station_data = data.get(station, {})
            station_data[key] = months_formatted
            data[station] = station_data

import_stations('./data/allstations.txt')
import_zipcodes('./data/zipcodes-normals-stations.txt')
import_temperatures('./data/mly-tmax-normal.txt', 'max_data')
import_temperatures('./data/mly-tmin-normal.txt', 'min_data')

WeatherLocation.objects.all().delete()

for key, val in data.iteritems():
    if not val.get('min_data') and not val.get('max_data'):
        continue

    data_dict = {
        'source': WeatherLocation.SOURCE_NOAA,
        'source_idenitifier': val['id'],
        'location': GEOSGeometry('POINT(%s %s)' % (val['longitude'], val['latitude']), srid=4269),
        'place_name': val.get('place_name', ''),
        'station_name': val.get('station_name', ''),
        'subnational_entity': val.get('state', ''),
        'country': 'US',
        'postal_code':  val.get('zipcode', ''),
        'min_data': val['min_data'],
        'max_data': val['max_data']
    }
    WeatherLocation.objects.create(**data_dict)
