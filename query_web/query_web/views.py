from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home(request):
    print("test function is called from views")
    return render(request,"home.html",{})