from functools import partial
from django.http.response import JsonResponse
from django.views.generic.base import View
from rest_framework.serializers import Serializer
from .models import Student
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Student_api(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body # get request body
        print('json_data: ', json_data)
        
        stream = io.BytesIO(json_data) # streams the request
        print('stream: ', stream)
        
        pythondata = JSONParser().parse(stream) # converting stream to python native data
        print('pythondata: ',pythondata)
        
        id = pythondata.get('id',None)
        
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            # json_data = JSONRenderer().render(serializer.data)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)

        if serializer.is_valid():
            serializer.save() # data created here

            # process to return response to myapp
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pythondata, partial=True)
        # for complete update
        # serializer = StudentSerializer(stu, data=pythondata)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,'content_type = application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,'content_type = application/json')


    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        print(id)
        if id:
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'msg': 'Data deleted'}
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data, 'content_type= application/jsonz')
            return JsonResponse(res, safe=False)
        # return JsonResponse(res, safe=False)




            
        



