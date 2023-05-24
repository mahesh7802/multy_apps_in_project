from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def app2_honey(request):
    return HttpResponse('<center><h1>this is app2_mahesh</h1></center>')


def app2_mahesh(request):
    return render(request,'app2_mahesh.html')
