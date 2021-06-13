
from typing import ByteString
from django.core.checks.messages import Error
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render
import os
import requests
import json
from rest_framework import serializers
from .constants import API_KEY
from .serializers import WeatherSerializer, LocationSerializer
from .models import Location, Weather, models
from rest_framework import viewsets


# API_KEY = 'ZmfG9LaR7j2DRHHNRamkw9vrGuwzFtSJaOOUynOe'


### RapidAPI ################

# url = "https://community-open-weather-map.p.rapidapi.com/find"

# querystring = {"q":"london","cnt":"1","mode":"null","lon":"0","type":"link, accurate","lat":"0","units":"imperial, metric"}

# headers = {
#     'x-rapidapi-key': "d8234bd417mshf392465fa12e61bp153129jsn3efa7c4a438b",
#     'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

#####################################

########## ambee #################
# API_KEY = 'ZmfG9LaR7j2DRHHNRamkw9vrGuwzFtSJaOOUynOe'

class LocationDetails(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class WeatherDetails(viewsets.ModelViewSet):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

def get_data(request):
    url = "https://api.ambeedata.com/weather/history/by-lat-lng"

    querystring = {
        "lat":"12.9889055",
        "lng":"77.574044",
        "from":"2020-07-13 12:16:44",
        "to":"2020-07-13 16:17:46"
        }
    headers = {
        'x-api-key': API_KEY,
        'Content-type': "application/json"
        }
    response = requests.request("GET", url, headers=headers, params=querystring).json() # returns dict
    # or
    # response = requests.get(url, headers=headers, params=querystring).json()
    # data_pyth = json.loads(response)

    # print(response, end='\n')

    # place_list = Location.objects.values('place')
    # print(list(place_list))
    place_vals = [place.get('place') for place in Location.objects.values('place')]
    
    if response.get('status') == 'success':
        data = response.get('data')
        history = data.get('history')
        hist = history[-1]
        # print(history)
        # print(Location.objects.values_list('lat'))
        print('\n')
    

        # for hist in history:
        temperature = hist.get('temperature')
        humidity = hist.get('humidity')
        pressure = hist.get('pressure')

        # print(str(data.get('lat')) + ' ' + str(data.get('lng')))    
        # print(Location.objects.values('place'))
        
        if (str(data.get('lat')) + ' ' + str(data.get('lng'))) in place_vals:
            print('Location data already present.')
        else:
            place = str(data.get('lat')) + ' ' + str(data.get('lng'))
            Location.objects.create(place=place)
            cnt_loc = Location.objects.count()
            try:
                l_id = Location.objects.get(pk=cnt_loc)

            except Exception as e:
                print('Error occured due to ',e )
            
            Weather.objects.create(location=l_id, stat_name='temperature', stat_value=str(temperature))
            Weather.objects.create(location=l_id, stat_name='humidity', stat_value=str(humidity))
            Weather.objects.create(location=l_id, stat_name='pressure', stat_value=str(pressure))
            print('records created')
            return HttpResponse('Values Returned')

    return HttpResponse('No Value found')

    ################# testing ###################
    # lat_set = set(Location.objects.values_list('lat'))
    # print(set(Location.objects.values_list('lat')))
    # print(Location.objects.values('lat'))
    # lats = Location.objects.values('lat')
    # for i in lats:
        # print(i.get('lat'))
    # print(Location.objects.values('place'))
    # place_list = Location.objects.values('place')
    # # print(list(place_list))
    # place_val = [place.get('place') for place in place_list]
    # print(place_val)
    # # for pl in place_list:
    # #     print(pl.get('place'))
    # return HttpResponse('Testing')
    # ###############################################