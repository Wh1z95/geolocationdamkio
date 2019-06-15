from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Localization

# Create your views here.
longitude = 23.1572891
latitude = 53.1328645

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Localization
    context_object_name = 'localizations'
    queryset = Localization.objects.annotate(distance=Distance('location',
                                                       user_location)
                                     ).order_by('distance')[0:6]
    template_name = 'localizations/index.html'
