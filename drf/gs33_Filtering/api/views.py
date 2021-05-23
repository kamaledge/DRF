from re import L
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='user1') : way 1
    # but the goal would be access the list of students passed by logged in users, so it won't work this way
    serializer_class = StudentSerializer

    # to achieve above requirement coventionally    : override get_queryset
    def get_queryset(self):
        # return super().get_queryset()
        user = self.request.user # capture current user sending request
        return Student.objects.filter(passby=user) # using the user for filter
