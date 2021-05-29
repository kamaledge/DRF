from django.contrib import admin
from django.urls import path, include
from django.utils.translation import deactivate
from api import views # type: ignore
from rest_framework.routers import DefaultRouter

# from rest_framework.authtoken.views import obtain_auth_token 
from api.auth import CustomAuthToken #type: ignore

# creating router router
router = DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest')), # for session authentication login prompt; a login tab appears. 
    path('gettoken/', CustomAuthToken.as_view()), # for token get/create
]