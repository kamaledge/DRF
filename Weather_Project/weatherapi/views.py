from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

# Create your views here.


def index(request):
    
    # url = 'api.openweathermap.org/data/2.5/weather?id={city id}&appid=08abc623de828d77996a749df4d980fc'
    
    url = 'api.openweathermap.org/data/2.5/weather?q={city name}&appid=08abc623de828d77996a749df4d980fc'
    
    cities = City.objects.values_list('name')

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()


    weather_data = []

    for city in cities:
        print(city)
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,

            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)
        print(weather_data)

    context = {'weather_data' : weather_data, 'form':form}
    return render(request, 'weatherapi/index.html', context)
