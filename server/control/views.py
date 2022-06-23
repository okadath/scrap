from django.shortcuts import render
from server.tasks import delayed_add
import time

# Create your views here.
def index(request):
	for counter in range(20):
		
		a=delayed_add.delay(3, counter)
		print(a)
	return HttpResponse("FINISH PAGE LOAD"+str(a))

	# if request.method == "POST":

	# else:
	# 	return render(request,"index.html")


from django.shortcuts import HttpResponse

# from .tasks import delayed_add

def celery_view(request):
	for counter in range(2):
		a=delayed_add.delay(3, counter)
		print(a)
	return HttpResponse("FINISH PAGE LOAD"+str(a))