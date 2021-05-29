from django.contrib import admin
from .models import Traveller

# Register your models here.

admin.site.register(Traveller)
# @admin.register(Traveller)
# class TravellerAdmin(admin.ModelAdmin):
#     list_display = ['id','name','age','country']
