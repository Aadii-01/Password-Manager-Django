from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random
# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello World</h1><br> <h3>This is my first Django project</h3>")

def home(request):
    return render(request, 'home.html')

def passgen(request):
    char = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get("uppercase"):
        char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("digits"):
        char.extend(list("123456789"))
    if request.GET.get("symbols"):
        char.extend(list("@#$%^&*()-_=+/*-"))
    
    length = int(request.GET.get("length",10))
    password = ""
    for x in range(length):
        password += random.choice(char)
    return render(request, 'password.html', {"password" : password})

