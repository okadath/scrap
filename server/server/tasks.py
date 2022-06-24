# from celery import shared_task
from server.celery import app

from .services import core
import time
from celery_singleton import Singleton

from celery.utils.log import get_task_logger



logger = get_task_logger(__name__)
# @shared_task(name='sum two numbers')
@app.task(base=Singleton)
def delayed_add():
	# for i in range(0,5):
		# time.sleep(1)
		# print(i)
	# logger.info(str(x)+"ab-"+str(y))
	result = core()
	
	return result