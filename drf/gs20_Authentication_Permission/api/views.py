from functools import partial
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework. permissions import AllowAny, IsAuthenticated, IsAdminUser


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes and permission_classes can be defined globally too, go to seetings.py.
    # When written at both places, the view one overrides setting one.
    authentication_classes = [BasicAuthentication] # by default here, the authentication is AllowAny. No login page given with below code.
    
    # permission_classes = [IsAuthenticated] # provides access to only authenticated users
    # by adding permission_classes, a login would be prompted while accessing API
    # Still, any user with proper credentials can access the API
    
    permission_classes = [AllowAny]

    # permission_classes = [IsAdminUser] # someone with IsStaffMember would be able to access 



