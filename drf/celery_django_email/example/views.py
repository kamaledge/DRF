from django.shortcuts import render, HttpResponse
from .task import *
# Create your views here.

def index(request):
    # sleepy()
    # sleepy.delay(10)
    # return HttpResponse('<h1>Task 1 done    </h1>')
    #  send_mail_task()
    #  send_mail_task()
    #  return HttpResponse('<h1>Email Sent</h1>')
     send_mail_task.delay() # delay calls out cellery,  makes it being handled by celery
     return HttpResponse('<h1>Email Sent via celery</h1>')
