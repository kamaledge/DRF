from django.shortcuts import render
import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body # body content of request
        print('json data is ',json_data)
        stream = io.BytesIO(json_data) # stream data
        print('stream is ',stream)
        pythondata = JSONParser().parse(stream) # python native data
        print('pythondata is ',pythondata)
        serializer = StudentSerializer(data=pythondata) # serializarion
        print('serializer is ',serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
        
            #way 1
            json_data = JSONRenderer().render(res) 
            return HttpResponse(json_data, content_type='application/json')

            # way 2
            # JsonResponse(msg,safe=False)
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')