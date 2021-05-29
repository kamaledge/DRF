from functools import partial
from django.http.response import JsonResponse
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

# Create your views here.
@csrf_exempt
def Student_api(request):
    if request.method == 'GET':
        json_data = request.body # get request body
        print('json_data: ', json_data)
        stream = io.BytesIO(json_data) # streams the request
        print('stream: ', stream)
        pythondata = JSONParser().parse(stream) # converting stream to python native data
        print('pythondata: ',pythondata)
        id = pythondata.get('id',None)
        print('id is :',id)
        if id is not None:
            stu = Student.objects.get(id=id)
            print('stu is :',stu)
            serializer = StudentSerializer(stu)
            print('serializer is', serializer)
            json_data = JSONRenderer().render(serializer.data)
            print('json data is : ', json_data)
            return HttpResponse(json_data, content_type='application/json')
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
    if request.method == 'POST':
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
    
    if request.method == 'PUT':
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
    
    if request.method == 'DELETE':
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




            
        



