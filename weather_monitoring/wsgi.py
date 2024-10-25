"""
WSGI config for weather_monitoring project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from weather.scheduler import start_scheduler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_monitoring.settings')

application = get_wsgi_application()
start_scheduler()
