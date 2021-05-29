from django.contrib import admin
from django.urls import path, include
from django.utils.translation import deactivate
from api import views # type: ignore
from rest_framework.routers import DefaultRouter

# creating router router
router = DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
