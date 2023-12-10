from django.http import HttpResponse
from django.shortcuts import render
from .models import Photo ,Album

# Create your views here.


def home(request):
    data = Album.objects.all()
    return render(request , 'images/home.html' ,{'data':data})