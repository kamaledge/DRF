
# Session Authentication

from functools import partial
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
# from rest_framework. permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .custompermissions import MyPermission


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    
    authentication_classes = [SessionAuthentication] 
    # no login prompt asked, and no access to API given
    # to proceed, we make some changes to urls.py

    # permission_classes = [IsAuthenticated] # anyone with user account
   
    # permission_classes = [AllowAny] # No login required
   
    # permission_classes = [IsAdminUser] # StaffMember
   
    # permission_classes = [IsAuthenticatedOrReadOnly] #read permissions to AuthenticatedUsers, and write and write permissions to Authenticated users
   
    # permission_classes = [DjangoModelPermissions] # grants read access to any user, for write permissions we need to give app->add, api->change permissions as per requirement via admin portal to the user

    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly] # feature of DjangoModelPermissions plus read access to UnAuthenticated Users   

    
    # Custom Permission Class Use
    permission_classes = [MyPermission]



