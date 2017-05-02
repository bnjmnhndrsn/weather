# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views import View

from weather.models import WeatherLocation
from weather.serializers import serialize_search, serialize_detail

def index(request):
    return render(request, 'weather/index.html', {})

class SearchView(View):
    def _filter_by_query(self, query):
        stripped = query.strip()

        query = Q(postal_code__istartswith=stripped) | Q(place_name__istartswith=stripped)
        return WeatherLocation.objects.filter(query).order_by('place_name', 'subnational_entity')[0:20]

    def get(self, request):
        results = []
        if 'query' in request.GET:
            results = self._filter_by_query(request.GET['query'])

        serialized = serialize_search(results)
        return JsonResponse(serialized, safe=False)

class WeatherLocationView(View):
    def get(self, request, *args, **kwargs):
        weather_location_id = kwargs.get('weather_location_id')
        weather_location = WeatherLocation.objects.get(pk=weather_location_id)
        serialized = serialize_detail(weather_location)
        return JsonResponse(serialized, safe=False)
