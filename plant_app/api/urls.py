
from django.contrib import admin
from django.urls import path, include
from plant_app.api.views import PlantAV, PlantDetailAV, PlantImageDetailAV
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('list/', PlantAV.as_view(), name='plant-list'),
    path('create/', PlantAV.as_view(), name='plant-create'),
    path('<int:pk>/', PlantDetailAV.as_view(), name='plant-detail'),
    path('<int:pk>/add-image/', PlantImageDetailAV.as_view(), name='plant-add-image'),
    path('<int:pk>/update/', PlantAV.as_view(), name='plant-update'),
]
