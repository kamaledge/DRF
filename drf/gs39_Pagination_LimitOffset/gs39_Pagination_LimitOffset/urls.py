
from django.contrib import admin
from django.urls import path
from api import views # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/' ,views.StudentList.as_view(), name='studentlist'),
]
