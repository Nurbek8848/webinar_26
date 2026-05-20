from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def task1(request):
    return render(request, "task1.html")


def task2(request):
    return render(request, "task2.html")


def task3(request):
    return render(request, "index.html")


def task4(request):
    return render(request, "task4.html")


def task5(request):
    return render(request, "index.html")
