from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_task():
    sleep(10)
    send_mail('Mail check','Mail using Celery','tiwari.kamal.nath1@gmail.com',['tiwari.kamal.nath@gmail.com'], fail_silently=False)

    return None

