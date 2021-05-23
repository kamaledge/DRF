from django.db import router
from django.urls import base, path, include
# type: ignore
from enroll.api import views # type: ignore
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('crud', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]