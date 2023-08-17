from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/",home),  
    path("solution/<int:id>",solution),
    path("do_solution/<int:id>",do_solution) 
]