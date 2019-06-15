from django.contrib.gis.admin import OSMGeoAdmin
from .models import Localization


@Admin.register(Localization)
class LocalizationAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')