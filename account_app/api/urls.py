from django.contrib import admin
from django.urls import path, include
from account_app.api.views import login_view

urlpatterns = [
    path('login-app/', login_view, name='login-app'),
    
]
