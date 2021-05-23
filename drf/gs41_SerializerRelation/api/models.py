from django.db import models
from django.db.models.deletion import CASCADE
# from django.db.models.enums import Choices

gender_choice = [('M', 'Male'), ('F', 'Female'), ('O', 'Others')] 

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=gender_choice)

    def __str__(self):
        # return super().__str__()
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=CASCADE, related_name='song') # related name is used to show the data of linked table too
    duration = models.IntegerField()

    def __str__(self):
        # return super().__str__()
        return self.title
    
