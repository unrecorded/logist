from django.contrib import admin
from geo.models import Geo, City, Transport, Paid, Status, Auto, Driver

# Register your models here.
@admin.register(Geo)
class GeoAdmin(admin.ModelAdmin):
    pass

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    pass

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass

@admin.register(Paid)
class PaidAdmin(admin.ModelAdmin):
    pass