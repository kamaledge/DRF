from django.db import models
from django.db.models.fields import AutoField
from django.utils.translation import deactivate

# Create your models here.

class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    # lat = models.FloatField()
    # lon = models.FloatField()
    place = models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.id) + ' ---- \'' + self.place + '\''
    
    # def __repr__(self):
    #     return str(self.id)


class Weather(models.Model):
    stat_name = models.CharField(max_length=100)
    stat_value = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='weather')

    def __str__(self):
        return self.stat_name +str(self.location)
    

