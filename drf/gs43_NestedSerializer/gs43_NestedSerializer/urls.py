
from django.contrib import admin
from django.db import router
from django.urls import path, include
from api import views # type: ignore
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('singer', views.SingerViewSet, basename='singer')
router.register('song', views.SongSerializer, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
