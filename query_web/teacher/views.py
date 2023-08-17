from django.shortcuts import render,redirect
from django.http import HttpResponse
from student.models import upload
# Create your views here.
def home(request):
    up = upload.objects.all()
    return render(request,"teacher/home.html",{
        'up':up
    })
def solution(request,id):
   emp =  upload.objects.get(id=id)
   return render(request,"teacher/upload_solution.html",{
        'stu':emp
    })
def do_solution(request,id):
    if request.method == "POST":
        teac_solution = request.POST.get("solution")
        docs = request.POST.get("docs")
        te =  upload.objects.get(id=id)
        te.solution = teac_solution
        te.docs = docs
        te.save()
    return redirect("/teacher/home/")
   