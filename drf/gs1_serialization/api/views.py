from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse

# Create your views here.

# Model object - Single Student Data

def Student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializers(stu) # serializer is a variable
    
    # way 1
    # json_data = JSONRenderer().render(serializer.data) # serializer is a variable
    # return HttpResponse(json_data,content_type='application/json')

    # way 2
    return JsonResponse(serializer.data)


# QuerySet - All Student Data

def Student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializers(stu,many=True)
    
    # way 1
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')

    # way 2
    return JsonResponse(serializer.data, safe=False) # safe false because here serializer data is not dict unlike model object above, it is list of dict rather
