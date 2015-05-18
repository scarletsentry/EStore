"""
WSGI config for EStore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import site

site.addsitedir('site.addsitedir('/home/fayt/.local/lib/python2.7/site-packages/')')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EStore.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
