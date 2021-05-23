from django.db import models

# Create your models here.

class Traveller(models.Model):
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    country = models.CharField(max_length=70)

    def __str__(self):
        return self.name
