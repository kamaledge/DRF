
# Session Authentication

from functools import partial
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework. permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import JackRateThrottle


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    
    authentication_classes = [SessionAuthentication] 

    permission_classes = [IsAuthenticatedOrReadOnly] 

    
    # setting up throttle, to control how many request can be sent by registered users and anonymous users
    
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    # throttle_classes = [AnonRateThrottle, JackRateThrottle]



