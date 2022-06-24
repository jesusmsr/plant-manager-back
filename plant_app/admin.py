from django.contrib import admin

from plant_app.models import Plant, PlantImage

# Register your models here.
admin.site.register(Plant)
admin.site.register(PlantImage)