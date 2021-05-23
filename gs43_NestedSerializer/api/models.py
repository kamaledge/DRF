from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

choice_gender = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Others'),
]
class Singer(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=choice_gender)

    def __str__(self):
        # return super().__str__()
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=50)
    singer = models.ForeignKey(Singer, on_delete=CASCADE, related_name='songssung')
    duration = models.IntegerField()

    def __str__(self):
        return self.title
    
