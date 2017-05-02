from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^json/search/$', views.SearchView.as_view()),
    url(r'^json/search/$', views.SearchView.as_view()),
    url(r'^json/locations/(?P<weather_location_id>\d+)/$', views.WeatherLocationView.as_view())

]
