from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1_string(request):
    return HttpResponse('<center><h1>HII THIS IS APP1_STRING REQUEST</h1></center>')


def app1_page(request):
    return render(request,'app1_page.html')