
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import views
from rest_framework.routers import DefaultRouter
from api import views # type: ignore

router = DefaultRouter()

router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
