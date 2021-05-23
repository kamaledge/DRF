from django.core.mail import send_mail

def sendmail_without_celery():
    send_mail('CELERY_WORKED_YEAH','CELERY IS COOL','tiwari.kamal.nath1@gmail.com',['tiwari.kamal.nath@gmail.com'],fail_silently=False)