"""
WSGI config for EStore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import site
import sys

proj_dir = os.path.dirname(__file__)
env_dir = "/home/fayt/.virtualenvs/EStore"

site.addsitedir('/home/fayt/.virtualenvs/EStore/lib/python2.7/site-packages')
sys.path.append(proj_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EStore.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
