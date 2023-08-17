from django.db import models

# Create your models here.

class Course(models.Model):
    course=models.CharField(max_length=200)
    name= models.CharField(max_length=200)

class upload(models.Model):
    name=models.CharField(max_length=50,default=" ")
    rollno=models.CharField(max_length=10,default=" ")
    query=models.CharField(max_length=500)
    image=models.ImageField(upload_to="media/upload/")
    solution=models.CharField(max_length=5000,default=" ",blank=True)

class students(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.CharField(max_length=20)