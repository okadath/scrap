from django.shortcuts import render
from server.tasks import delayed_add,delayed_bot
import time

from django.shortcuts import HttpResponse

# from .tasks import delayed_add
from celery.result import AsyncResult

import os

# Create your views here.
def index(request):
	# a=" none"
		# res = AsyncResult(a.task_id)
		# print(res.ready())
	if request.method == "POST":
		# print(request.POST)
		print("<sas")
		os.system("/home/okadath/Desktop/python/bot_local/venv/bin/python /home/okadath/Desktop/python/bot_local/bot.py")

		# for counter in range(2):
		# delayed_bot.delay()
		# for counter in range(2):
			# delayed_add.delay(3, counter)
			# print(a)
	# 	res = AsyncResult(a.task_id)
	# 	print(res.ready())
	return render(request, 'index.html')

	# return HttpResponse("FINISH PAGE LOAD"+str(a))

	# if request.method == "POST":

	# else:
	# 	return render(request,"index.html")


# def celery_view(request):
# 	for counter in range(2):
# 		a=delayed_add.delay(3, counter)
# 		# print(a)
# 		res = AsyncResult(a.task_id)
# 		print(res.ready())
# 	return HttpResponse("FINISH PAGE LOAD"+str(a))