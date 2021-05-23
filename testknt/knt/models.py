
from django.db import models



# For database with existing table mapping
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    class Meta:
       managed = False
       db_table = 'PERSON_OR' # mapping to existing table 'PERSON_OR'

# print(Person.__init__)

# creating new table in database named 'knt_Person2'    
class Person2(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
