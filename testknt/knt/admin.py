from django.contrib import admin
from .models import Person, Person2
# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']

@admin.register(Person2)
class Person2Admin(admin.ModelAdmin):
    list_display = ['id', 'first_name']

