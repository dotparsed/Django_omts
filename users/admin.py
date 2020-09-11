from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . models import Profile
from .models import Order
from .models import City

admin.site.register(Profile)
admin.site.register(Order)

@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    pass