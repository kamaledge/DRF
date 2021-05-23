"""
WSGI config for gs22_Authentication_Perm_CustomPermissions project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs22_Authentication_Perm_CustomPermissions.settings')

application = get_wsgi_application()
