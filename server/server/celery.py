from __future__ import absolute_import  
import os  
from django.conf import settings  
from celery import Celery

# set default Django settings module for celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# app = Celery('server_tasks', broker=settings.CELERY_BROKER_URL)
# app.config_from_object('django.conf:settings', namespace='CELERY')  
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
app = Celery('server_tasks') #Nota 1
app.config_from_object('django.conf:settings', namespace='CELERY') #Nota 2
app.autodiscover_tasks() #Nota 3
