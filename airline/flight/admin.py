from django.contrib import admin
from .models import Flight,Airport,Pasanger
# Register your models here.
class Flightadmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")

class Passangeradmin(admin.ModelAdmin):
    filter_horizontal=("flight",)

class Airportadmin(admin.ModelAdmin):
    list_display = ("code","city")

admin.site.register(Airport,Airportadmin)
admin.site.register(Flight,Flightadmin)
admin.site.register(Pasanger,Passangeradmin)