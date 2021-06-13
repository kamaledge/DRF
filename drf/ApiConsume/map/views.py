from django.http.response import JsonResponse
from django.shortcuts import render
import requests
from requests.api import head

# Create your views here.
url = 'https://positioning.hereapi.com/'
get_res = '/v2/locate?apiKey=Hddt22ilYkb11r4XsRHznUkORj2KYLSIDZTKhGwWjB8'

def get_map(request):
    loc = requests.request(method='POST', url=url+get_res, headers= {'Content-Type': 'application/json'}, params={
  "wlan": [
    {
      "mac": "36:68:95:1A:36:93",
      "rss": -74
    }, 
    {
      "mac": "18:64:72:B7:BC:B2",
      "rss": -75
    },
    {
      "mac": "18:64:72:B7:89:21",
      "rss": -76
    },
    {
      "windows": "2405:201:a402:6028:a981:1c45:649d:173b",
      "rss": -77
    },
    {
      "mac": "18:64:72:B7:B1:63",
      "rss": -79
    }
  ]
})
    return JsonResponse(loc.json)
    

# https://developer.here.com/documentation/positioning-api/dev_guide/topics/construct-locate-request.html
