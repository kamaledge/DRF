from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Traveller
from .serializers import TravellerSerializer
# Create your views here.

class T_LCapi(ListCreateAPIView):
    queryset = Traveller.objects.all()
    serializer_class = TravellerSerializer


class T_RUDapi(RetrieveUpdateDestroyAPIView):
    queryset = Traveller.objects.all()
    serializer_class = TravellerSerializer