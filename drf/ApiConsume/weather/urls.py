from os import name
from rest_framework import routers
from .views import get_data, LocationDetails, WeatherDetails
from django.urls import path, include

router = routers.DefaultRouter()


router.register('location', LocationDetails, basename='loc')
router.register('weather', WeatherDetails, basename='wea')

urlpatterns = [
    # path('api/',include(router.urls)),
    path('result',get_data),
    path('', include(router.urls), name = 'api'),
]