from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Course,upload

# Create your views here.
def home(request):
    cor = Course.objects.all()
    return render(request,"student/home.html",{
        'cor':cor
    })

def course(request):
    
    upl= upload.objects.all()
    return render(request,"student/course.html",{
        'upl':upl
    })

def upload_query(request):
    if request.method=='POST':
        name=request.POST.get("name")
        rollno=request.POST.get("rollno")
        query=request.POST.get("query")
        image = request.POST.get("image")

        upl=upload()

        upl.name=name
        upl.rollno=rollno
        upl.query=query
        upl.image=image

        upl.save()
        return redirect("/student/course/")
    return render(request,"student/upload_query.html",{})

def solution(request,id):
    sol=upload.objects.get(id=id)

    return render(request,"student/solution.html",{"sol":sol})
