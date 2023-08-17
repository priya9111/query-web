from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("home/",home),  
    path("course/",course),
    path("upload_query/",upload_query),
    path("solution/<int:id>",solution)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)