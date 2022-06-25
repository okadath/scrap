# from celery import shared_task
from server.celery import app

from .services import core,add
import time
from celery_singleton import Singleton

from celery.utils.log import get_task_logger



logger = get_task_logger(__name__)
# @shared_task(name='sum two numbers')
@app.task(base=Singleton)
def delayed_add(x,y):
	# for i in range(0,5):
		# time.sleep(1)
		# print(i)
	result = add(x, y) 
	# logger.info("4ab-")
	# result = core()
	
	return result

@app.task(base=Singleton)
def delayed_bot():
	# for i in range(0,5):
		# time.sleep(1)
		# print(i)
	# result = add(x, y) 
	# logger.info("4ab-")
	result = core()
	
	return result