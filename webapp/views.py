from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def task3(request):
    return render(request, "index.html")
