# from celery import shared_task
from server.celery import app

from .services import add
import time

from celery.utils.log import get_task_logger



logger = get_task_logger(__name__)
# @shared_task(name='sum two numbers')
@app.task
def delayed_add(x, y):
	time.sleep(20)
	# print(x)
	logger.info(str(x)+"ab-"+str(y))
	result = add(x, y)
	
	return result