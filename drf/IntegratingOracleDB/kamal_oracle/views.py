from typing import ByteString
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .serializers import KntPerson2Serializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import KntPerson2
import io

# Create your views here.
class KntPerson2details(viewsets.ModelViewSet):
    queryset = KntPerson2.objects.all()
    serializer_class = KntPerson2Serializer

def getdatafromsql(request):
    res = []
    for p in KntPerson2.objects.raw('select id from KNT_DETAIL'):  # queryset
        # the raw sql can contain other tablenames too, raw query must include primarykey
        # However, extra columns won't show up, as above, and first 2 columns if defined in KntPerson2 model as such would show
        
        # print(p)
        serializer = KntPerson2Serializer(p) # queryset converted to python native datatype
        print(serializer.data)
        res.append(serializer.data)
    

    return JsonResponse(res, safe=False) # python native data rendered as json
