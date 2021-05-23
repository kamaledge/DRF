"""
WSGI config for gs14_ClassBased_GeneicAPI_Mixins_CRUD project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs14_ClassBased_GeneicAPI_Mixins_CRUD.settings')

application = get_wsgi_application()
