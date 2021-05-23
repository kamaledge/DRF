from re import L
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter, SearchFilter

# Create your views here.

# We can use th combinatiosn fo filter backends too

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city']
    # filterset_fields = ['name','city']
    # filter_backends = [SearchFilter]
    filter_backends = [OrderingFilter] # without ordering fields, it provided us the ordering filter in browsable API, with all the ordering options
    # search_fields = ['city']
    # search_fields = ['name','city']
    # search_fields = ['^name']
    ordering_fields = ['name'] # restricts the ordering field keys in the browsable API

    
   
