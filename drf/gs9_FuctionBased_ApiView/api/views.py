from requests import api
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
# GET
# @api_view() # by default HttpMethod is GET
# def hello_world(request):
#     return Response({'msg': 'Hello World'})

# GET
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'Hello World'})

# POST
# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data) # {'name': 'Rai', 'roll': 112, 'city': 'Ranchi'}
#         return Response({'msg': 'This is post request'})


@api_view(['GET', 'POST']) # give access to browsable API too
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'This is GET request'})
    if request.method == 'POST':
        print(request.data) # {'name': 'Rai', 'roll': 112, 'city': 'Ranchi'}
        return Response({'msg': 'This is POST request', 'data': request.data})
















# Request objects
# REST framework introduces a Request object that extends the regular HttpRequest, and provides more flexible request parsing. The core functionality of the Request object is the request.data attribute, which is similar to request.POST, but more useful for working with Web APIs.

# request.POST  # Only handles form data.  Only works for 'POST' method.
# request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.
# Response objects
# REST framework also introduces a Response object, which is a type of TemplateResponse that takes unrendered content and uses content negotiation to determine the correct content type to return to the client.

# return Response(data)  # Renders to content type as requested by the client.
