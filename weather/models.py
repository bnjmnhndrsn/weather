# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.postgres.fields import JSONField

class WeatherLocation(models.Model):
    SOURCE_NOAA = 10

    SOURCES = (
        (SOURCE_NOAA, 'NOAA'),
    )

    source = models.IntegerField(choices=SOURCES)
    source_idenitifier = models.CharField(max_length=30)
    location = PointField(srid=4269)
    place_name = models.CharField(null=False, blank=True, max_length=30)
    station_name = models.CharField(null=False, blank=True, max_length=30)
    subnational_entity = models.CharField(null=False, blank=True, max_length=30)
    country = models.CharField(null=False, blank=False, max_length=30)
    postal_code = models.CharField(null=False, blank=True, max_length=30)
    min_data = JSONField(default=list)
    max_data = JSONField(default=list)
