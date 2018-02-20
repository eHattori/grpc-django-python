"""
WSGI config for myapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from startup import server_context

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")

application = get_wsgi_application()
