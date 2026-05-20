from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def task1(request):
    return render(request, "task1.html")


def task2(request):
    return render(request, "task2.html")
