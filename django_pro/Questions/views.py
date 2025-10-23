from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def quest1(request):
    return render(request,"questions/question1.html")

def quest2(request):
    return render(request,"questions/question2.html")