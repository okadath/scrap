# from django.conf.urls import url
from django.urls import path, include
from control import views

urlpatterns = [
    # path('',views.home,name='home'), 
    path('',views.index,name='home'),
 
]
