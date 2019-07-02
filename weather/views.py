# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views import View
from django.contrib.gis.db.models import functions
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis import measure

from weather.models import WeatherLocation
from weather.serializers import serialize_search, serialize_detail

MAX_MILE_DISTANCE = 15

def index(request):
    return render(request, 'weather/index.html', {})

class SearchView(View):
    def _filter_by_query(self, query):
        stripped = query.strip()

        query = Q(postal_code__istartswith=stripped) | Q(place_name__istartswith=stripped)
        return WeatherLocation.objects.filter(query).order_by('place_name', 'subnational_entity')[0:20]

    def _filter_by_lat_lng(self, lat, lng):
        try:
            location = GEOSGeometry('POINT(%s %s)' % (lng, lat), srid=4269)
        except ValueError:
            return

        return WeatherLocation.objects.annotate(
            distance=Distance('location', location)
        ).order_by('distance')[0:20]

    def get(self, request):
        results = []
        if 'query' in request.GET:
            results = self._filter_by_query(request.GET['query'])

        if 'lat' in request.GET and 'lng' in request.GET:
            results = self._filter_by_lat_lng(request.GET['lat'], request.GET['lng'])

        serialized = serialize_search(results)
        return JsonResponse(serialized, safe=False)

class SearchByLocationView(View):
    def get(self, request):
        results = []
        if not 'lat' in request.GET and not 'lng' in request.GET:
            return JsonResponse({'error': 'missing lat/lng'}, status=400)

        try:
            location = GEOSGeometry('POINT(%s %s)' % (request.GET['lng'], request.GET['lat']), srid=4269)
        except ValueError:
            return JsonResponse({'error': 'invalid lat/lng'}, status=400)


        result = WeatherLocation.objects.annotate(
            distance=functions.Distance('location', location)
        ).order_by('distance').first()

        if not result:
            return JsonResponse({'error': 'no matches'}, status=400)

        if result.distance.mi > MAX_MILE_DISTANCE:
            return JsonResponse({'error': 'no matches within {} miles'.format(MAX_MILE_DISTANCE)}, status=400)

        serialized = serialize_detail(result)
        return JsonResponse(serialized, safe=False)

class WeatherLocationView(View):
    def get(self, request, *args, **kwargs):
        weather_location_id = kwargs.get('weather_location_id')
        weather_location = WeatherLocation.objects.get(pk=weather_location_id)
        serialized = serialize_detail(weather_location)
        return JsonResponse(serialized, safe=False)
