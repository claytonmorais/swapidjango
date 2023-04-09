from django.contrib import admin

# Register your models here.
from api.models import (
    Planet,
    People,
    Species,
    Starship,
    Vehicle,
    Film,
    Historic
)

admin.site.register(Planet)
admin.site.register(People)
admin.site.register(Species)
admin.site.register(Starship)
admin.site.register(Vehicle)
admin.site.register(Film)
admin.site.register(Historic)