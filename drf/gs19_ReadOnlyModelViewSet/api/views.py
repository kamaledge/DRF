from functools import partial
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # the above little code takes care of entire READ ONLY operations, ie list and retrieve