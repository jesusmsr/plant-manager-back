
from django.contrib import admin
from django.urls import path, include
from plant_app.api.views import PlantAV
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('list/', PlantAV.as_view(), name='plant-list'),
    path('create/', PlantAV.as_view(), name='plant-create'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
